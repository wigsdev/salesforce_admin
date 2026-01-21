from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.lumina import LuminaService
from app.dependencies import get_current_user
from app.models.user import User
from app.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Initialize Service (Singleton-ish for this context)
# In a real app we might use dependency injection for the service too
lumina_service = LuminaService(content_root="content")

from sqlalchemy.orm import Session
from app.database import get_db

@router.get("/progress", response_model=dict)
async def get_lumina_progress(db: Session = Depends(get_db)):
    """
    API Endpoint: Get calculated progress for Lumina Tech project (DB).
    """
    return lumina_service.get_stats(db)

@router.post("/tasks/{task_id}/toggle")
async def toggle_task(task_id: int, db: Session = Depends(get_db)):
    """
    Toggle task completion status.
    """
    stats_update = lumina_service.toggle_task(db, task_id)
    return stats_update

@router.get("/dashboard", response_class=HTMLResponse)
async def lumina_dashboard(request: Request, db: Session = Depends(get_db)):
    """
    Frontend View: Render the Lumina Tech Project Dashboard.
    Public endpoint: Auth is handled client-side by base.html
    """
    # Fetch data directly for SSR
    stats = lumina_service.get_stats(db)
    
    return templates.TemplateResponse(
        "lumina_dashboard.html", 
        {
            "request": request, 
            "user": None, # Auth handled client-side
            "stats": stats,
            "title": "Dashboard Lumina Tech"
        }
    )
