from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.lumina import LuminaDeliverable, LuminaTask

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# --- Pydantic Schemas for Request Body ---


class DayCreate(BaseModel):
    title: str
    reference: str = ""


class TaskCreate(BaseModel):
    description: str


class DayUpdate(BaseModel):
    title: Optional[str] = None
    reference: Optional[str] = None


# --- Endpoints ---


@router.get("/days")
def get_days(db: Session = Depends(get_db)):
    """Get all Lumina Days (Deliverables) with tasks ordered by ID."""
    days = db.query(LuminaDeliverable).order_by(LuminaDeliverable.id).all()
    # Serialize manually or rely on Pydantic response_model if configured,
    # but for simplicity in hybrid templates we can return dicts
    return [
        {
            "id": d.id,
            "title": d.title,
            "reference": d.reference,
            "tasks": [
                {"id": t.id, "desc": t.description, "done": t.is_completed}
                for t in d.tasks
            ],
        }
        for d in days
    ]


@router.post("/days")
def create_day(day_in: DayCreate, db: Session = Depends(get_db)):
    """Create a new Day."""
    new_day = LuminaDeliverable(
        title=day_in.title,
        reference=day_in.reference or "Sin referencia",
    )
    db.add(new_day)
    db.commit()
    db.refresh(new_day)
    return {
        "id": new_day.id,
        "title": new_day.title,
        "reference": new_day.reference,
        "tasks": [],
    }


@router.delete("/days/{day_id}")
def delete_day(day_id: int, db: Session = Depends(get_db)):
    """Delete a day and its tasks."""
    day = db.query(LuminaDeliverable).filter(LuminaDeliverable.id == day_id).first()
    if day:
        db.delete(day)
        db.commit()
    return {"success": True}


@router.put("/days/{day_id}")
def update_day(day_id: int, day_in: DayUpdate, db: Session = Depends(get_db)):
    """Update day title or reference."""
    day = db.query(LuminaDeliverable).filter(LuminaDeliverable.id == day_id).first()
    if not day:
        raise HTTPException(status_code=404, detail="Day not found")

    if day_in.title is not None:
        day.title = day_in.title
    if day_in.reference is not None:
        day.reference = day_in.reference

    db.commit()
    return {"success": True}


@router.post("/days/{day_id}/tasks")
def create_task(day_id: int, task_in: TaskCreate, db: Session = Depends(get_db)):
    """Add a task to a day."""
    new_task = LuminaTask(
        deliverable_id=day_id, description=task_in.description, is_completed=False
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
        "id": new_task.id,
        "desc": new_task.description,
        "done": new_task.is_completed,
    }


@router.put("/tasks/{task_id}/toggle")
def toggle_task_status(task_id: int, db: Session = Depends(get_db)):
    """Toggle task status."""
    task = db.query(LuminaTask).filter(LuminaTask.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.is_completed = not task.is_completed
    db.commit()
    return {"id": task.id, "done": task.is_completed}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task."""
    task = db.query(LuminaTask).filter(LuminaTask.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return {"success": True}
