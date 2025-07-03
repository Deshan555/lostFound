from pydantic import BaseModel, Field
from typing import Any, Optional, List
from datetime import datetime
import uuid

class CustomResponse(BaseModel):
    traceid: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    message: str
    data: Any
    status: bool = True

    class Config:
        from_attributes = True

class CustomErrorResponse(BaseModel):
    traceid: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    message: str
    data: Any = []
    status: bool = False

    class Config:
        from_attributes = True

class LostRecordFilter(BaseModel):
    itemType: Optional[str] = None
    dateLost: Optional[List[str]] = None
    locationLost: Optional[str] = None