from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateElectronicItemSchema(BaseModel):
    id: Optional[int] = None
    item_type: str
    record_type: str
    description: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    color: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateElectronicItemSchema(BaseModel):
    item_type: Optional[str] = None
    record_type: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    color: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateElectronicItemStatusSchema(BaseModel):
    record_type: str