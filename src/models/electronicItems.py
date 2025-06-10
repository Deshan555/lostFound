from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from src.config.database import Base
from enum import Enum

class RecordType(str, Enum):
    LOST = "lost"
    FOUND = "found"

class ElectronicItemType(str, Enum):
    PHONE = "phone"
    LAPTOP = "laptop"
    TABLET = "tablet"
    CAMERA = "camera"
    OTHER = "other"

class ElectronicItem(Base):
    __tablename__ = "electronic_items"
    id = Column(Integer, primary_key=True, index=True)
    item_type = Column(SQLEnum(ElectronicItemType), nullable=False)
    record_type = Column(SQLEnum(RecordType), nullable=False)
    description = Column(String(255), nullable=False)
    brand = Column(String(50), nullable=True)
    model = Column(String(50), nullable=True)
    serial_number = Column(String(50), nullable=True)
    color = Column(String(50), nullable=True)
    image_url = Column(String(255), nullable=True)
    image_url_2 = Column(String(255), nullable=True)
    image_url_3 = Column(String(255), nullable=True)