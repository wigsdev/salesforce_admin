from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.sprint import Sprint
from app.schemas.curriculum import SprintResponse

router = APIRouter()

@router.get("/sprints", response_model=List[SprintResponse])
def get_sprints(db: Session = Depends(get_db)):
    """
    Get all sprints with their tasks.
    """
    sprints = db.query(Sprint).order_by(Sprint.number).all()
    return sprints
