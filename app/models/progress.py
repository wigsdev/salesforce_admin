"""
UserProgress model for tracking user completion of tasks.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database import Base


class UserProgress(Base):
    """
    UserProgress model for tracking task completion.
    
    Attributes:
        id: Primary key
        user_id: Foreign key to User
        task_id: Foreign key to Task
        status: Completion status (not_started, in_progress, completed)
        started_at: When the user started the task
        completed_at: When the user completed the task
        notes: User notes about the task
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """
    
    __tablename__ = "user_progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(20), default="not_started", nullable=False)  # not_started, in_progress, completed
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="progress")
    task = relationship("Task", back_populates="progress")
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('user_id', 'task_id', name='uq_user_task'),
    )
    
    def __repr__(self):
        return f"<UserProgress(user_id={self.user_id}, task_id={self.task_id}, status='{self.status}')>"
