from pydantic import BaseModel, EmailStr
from typing import Optional

class createDocumentSchema(BaseModel):
    document_type: Optional[str] = None
    record_status: Optional[str] = None
    description: Optional[str] = None
    issuing_authority: Optional[str] = None
    document_number: Optional[str] = None
    owner_name: Optional[str] = None

class updateDocumentSchema(BaseModel):
    document_type: Optional[str] = None
    record_status: Optional[str] = None
    description: Optional[str] = None
    issuing_authority: Optional[str] = None
    document_number: Optional[str] = None
    owner_name: Optional[str] = None

class updateDocumentStatusSchema(BaseModel):
    record_status: str