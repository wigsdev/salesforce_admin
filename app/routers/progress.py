"""
Progress tracking API endpoints.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_active_user
from app.models.user import User
from app.schemas.progress import (
    ProgressCreate,
    ProgressResponse,
    SprintProgressResponse,
    UserProgressSummary
)
from app.services.progress_service import ProgressService

router = APIRouter()


@router.get("/me", response_model=List[ProgressResponse])
def get_my_progress(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get all progress for current user.
    
    Args:
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        List of progress records
    """
    progress = ProgressService.get_user_progress(db, current_user.id)
    return progress


@router.post("/mark", response_model=ProgressResponse)
def mark_task_progress(
    progress_data: ProgressCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Mark a task with status (not_started, in_progress, completed).
    
    Args:
        progress_data: Progress data with task_id and status
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        Updated progress record
        
    Raises:
        HTTPException: If task not found or invalid status
    """
    try:
        progress = ProgressService.mark_task(
            db,
            current_user.id,
            progress_data.task_id,
            progress_data.status,
            progress_data.notes
        )
        return progress
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/sprint/{sprint_id}", response_model=SprintProgressResponse)
def get_sprint_progress(
    sprint_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get progress summary for a sprint.
    
    Args:
        sprint_id: Sprint ID
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        Sprint progress summary
    """
    progress = ProgressService.get_sprint_progress(db, current_user.id, sprint_id)
    return progress


@router.get("/team", response_model=List[UserProgressSummary])
def get_team_progress(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get progress for all users in current user's team.
    
    Args:
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        List of user progress summaries
    """
    progress = ProgressService.get_team_progress(db, current_user.team)
    return progress
