from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: str
    markdown_path: str

class TaskResponse(TaskBase):
    id: int
    sprint_id: int
    due_date: Optional[datetime] = None
    created_at: datetime
    
    model_config = {"from_attributes": True}

class SprintBase(BaseModel):
    name: str
    description: Optional[str] = None
    number: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class SprintResponse(SprintBase):
    id: int
    tasks: List[TaskResponse] = []
    
    model_config = {"from_attributes": True}
