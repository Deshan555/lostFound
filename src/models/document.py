from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from src.config.database import Base
from enum import Enum

class LostRecordStatusEnum(str, Enum):
    LOST = "lost"
    FOUND = "found"

class DocumentType(str, Enum):
    ID_CARD = "id_card"
    PASSPORT = "passport"
    LICENSE = "license"
    CERTIFICATE = "certificate"
    OTHER = "other"

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(SQLEnum(DocumentType), nullable=False)
    record_status = Column(SQLEnum(LostRecordStatusEnum), nullable=False)
    description = Column(String(255), nullable=False)
    issuing_authority = Column(String(50), nullable=True)
    document_number = Column(String(50), nullable=True)
    owner_name = Column(String(100), nullable=True)
