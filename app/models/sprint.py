"""
Sprint model for course structure.
"""

from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Text, Date, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Sprint(Base):
    """
    Sprint model representing a course sprint/module.
    
    Attributes:
        id: Primary key
        number: Sprint number (1, 2, 3, 4)
        name: Sprint name (e.g., "Fundamentos y Seguridad")
        description: Detailed description of the sprint
        start_date: Sprint start date
        end_date: Sprint end date
        is_active: Whether this sprint is currently active
        created_at: Timestamp of creation
    """
    
    __tablename__ = "sprints"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    tasks = relationship("Task", back_populates="sprint", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Sprint(number={self.number}, name='{self.name}', active={self.is_active})>"
