"""
Task model for course assignments and classes.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Task(Base):
    """
    Task model representing a class, assignment, or superbadge.

    Attributes:
        id: Primary key
        sprint_id: Foreign key to Sprint
        category: Task category (Clase, Superbadge, Practica)
        title: Task title
        description: Detailed description
        markdown_path: Relative path to the markdown file
        order_index: Order within the sprint
        created_at: Timestamp of creation
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    sprint_id = Column(
        Integer, ForeignKey("sprints.id", ondelete="CASCADE"), nullable=False
    )
    category = Column(
        String(50), nullable=False, index=True
    )  # Clase, Superbadge, Practica
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    markdown_path = Column(String(500), nullable=False, unique=True)
    order_index = Column(Integer, default=0)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    sprint = relationship("Sprint", back_populates="tasks")
    progress = relationship(
        "UserProgress", back_populates="task", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', category='{self.category}')>"
