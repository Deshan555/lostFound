from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from src.config.database import Base
from enum import Enum

class LostRecordStatusEnum(str, Enum):
    LOST = "lost"
    FOUND = "found"

class JewelryType(str, Enum):
    RING = "ring"
    NECKLACE = "necklace"
    BRACELET = "bracelet"
    EARRINGS = "earrings"
    WATCH = "watch"
    OTHER = "other"

class MaterialType(str, Enum):
    GOLD = "gold"
    SILVER = "silver"
    PLATINUM = "platinum"
    DIAMOND = "diamond"
    OTHER = "other"

class Jewelry(Base):
    __tablename__ = "jewelry_items"

    id = Column(Integer, primary_key=True, index=True)
    jewelry_type = Column(SQLEnum(JewelryType), nullable=False)
    record_status = Column(SQLEnum(LostRecordStatusEnum), nullable=False)
    description = Column(String(255), nullable=False)
    brand = Column(String(50), nullable=True)
    model = Column(String(50), nullable=True)
    color = Column(String(50), nullable=True)
    material = Column(SQLEnum(MaterialType), nullable=False)
    weight = Column(String(50), nullable=True)
    image_url = Column(String(255), nullable=True)
    image_url_2 = Column(String(255), nullable=True)
    image_url_3 = Column(String(255), nullable=True)
