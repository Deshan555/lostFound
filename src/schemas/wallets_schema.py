from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateWalletSchema(BaseModel):
    item_type: str
    record_type: str
    description: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateWalletSchema(BaseModel):
    item_type: Optional[str] = None
    record_type: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class updateRecordStatusSchema(BaseModel):
    record_type: Optional[str] = None