# from sqlalchemy import Column, Integer, String, Enum as SQLEnum
# from src.config.database import Base
# from enum import Enum
#
# class LostRecordStatusEnum(str, Enum):
#     LOST = "lost"
#     FOUND = "found"
#
# class JewelryType(str, Enum):
#     RING = "ring"
#     NECKLACE = "necklace"
#     BRACELET = "bracelet"
#     EARRINGS = "earrings"
#     WATCH = "watch"
#     OTHER = "other"
#
# class MaterialType(str, Enum):
#     GOLD = "gold"
#     SILVER = "silver"
#     PLATINUM = "platinum"
#     DIAMOND = "diamond"
#     OTHER = "other"
#
# class Jewelry(Base):
#     __tablename__ = "jewelry_items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     jewelry_type = Column(SQLEnum(JewelryType), nullable=False)
#     record_status = Column(SQLEnum(LostRecordStatusEnum), nullable=False)
#     description = Column(String(255), nullable=False)
#     brand = Column(String(50), nullable=True)
#     model = Column(String(50), nullable=True)
#     color = Column(String(50), nullable=True)
#     material = Column(SQLEnum(MaterialType), nullable=False)
#     weight = Column(String(50), nullable=True)
#     image_url = Column(String(255), nullable=True)
#     image_url_2 = Column(String(255), nullable=True)
#     image_url_3 = Column(String(255), nullable=True)

from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateJewelrySchema(BaseModel):
    jewelry_type: str
    record_status: str
    description: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    material: str
    weight: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateJewelrySchema(BaseModel):
    jewelry_type: Optional[str] = None
    record_status: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    weight: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None

class UpdateJewelryStatusSchema(BaseModel):
    record_status: str

