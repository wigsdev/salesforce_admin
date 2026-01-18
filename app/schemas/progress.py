"""
Pydantic schemas for Progress model.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ProgressBase(BaseModel):
    """Base progress schema."""
    status: str = Field(..., pattern="^(not_started|in_progress|completed)$")
    notes: Optional[str] = None


class ProgressCreate(ProgressBase):
    """Schema for creating/updating progress."""
    task_id: int


class ProgressResponse(ProgressBase):
    """Schema for progress response."""
    id: int
    user_id: int
    task_id: int
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}


class SprintProgressResponse(BaseModel):
    """Schema for sprint progress summary."""
    sprint_id: int
    total_tasks: int
    completed: int
    in_progress: int
    not_started: int
    completion_percentage: float


class UserProgressSummary(BaseModel):
    """Schema for user progress summary in team view."""
    user_id: int
    user_name: str
    user_email: str
    completed: int
    in_progress: int
    not_started: int
    total_tasks: int
    completion_percentage: float
