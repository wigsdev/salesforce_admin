"""
Lumina Tech Project Models.
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel, TimestampMixin


class LuminaDeliverable(BaseModel, TimestampMixin):
    __tablename__ = "lumina_deliverables"

    title = Column(String, nullable=False)
    reference = Column(
        String, nullable=False
    )  # Renamed from path, used as subtitle/reference
    source_link = Column(String, nullable=True)

    # Relationships
    tasks = relationship(
        "LuminaTask",
        back_populates="deliverable",
        cascade="all, delete-orphan",
        order_by="LuminaTask.id",
    )


class LuminaTask(BaseModel, TimestampMixin):
    __tablename__ = "lumina_tasks"

    deliverable_id = Column(
        Integer, ForeignKey("lumina_deliverables.id"), nullable=False, index=True
    )
    description = Column(String, nullable=False)
    # doc_path is already in the DB from previous migration, but wasn't in the file I viewed?
    # Wait, looking at previous view_file of models/lumina.py (Step 11882), doc_path WAS MISSING in line 34-36. 
    # Ah, I see "doc_path = Column(String, nullable=True) # New field for documentation link" in the diff in Step 11877 removal!
    # I accidentally removed it! I must restore it.
    doc_path = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    
    # The TimestampMixin already provides created_at and updated_at.
    # No need to redefine them here.
    # created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    deliverable = relationship("LuminaDeliverable", back_populates="tasks")
