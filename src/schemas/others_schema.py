from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUndefinedLostItemSchema(BaseModel):
    item_type: str
    record_type: str
    description: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateUndefinedLostItemSchema(BaseModel):
    item_type: Optional[str] = None
    record_type: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateUndefinedLostItemStatusSchema(BaseModel):
    record_type: str