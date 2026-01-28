"""
Lumina Tech Project Models.
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel, TimestampMixin


class LuminaDeliverable(BaseModel, TimestampMixin):
    __tablename__ = "lumina_deliverables"

    title = Column(String, nullable=False)
    path = Column(String, unique=True, nullable=False, index=True)
    role = Column(String, nullable=False, index=True)
    weight = Column(Integer, default=10, nullable=False)

    # Relationships
    tasks = relationship(
        "LuminaTask", back_populates="deliverable", cascade="all, delete-orphan"
    )


class LuminaTask(BaseModel, TimestampMixin):
    __tablename__ = "lumina_tasks"

    deliverable_id = Column(
        Integer, ForeignKey("lumina_deliverables.id"), nullable=False, index=True
    )
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)

    # Relationships
    deliverable = relationship("LuminaDeliverable", back_populates="tasks")
