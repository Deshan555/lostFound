from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from src.config.database import Base
from enum import Enum

class RecordType(str, Enum):
    LOST = "lost"
    FOUND = "found"

class ItemType(str, Enum):
    WALLET = "wallet"
    BAG = "bag"
    OTHER = "other"


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    item_type = Column(SQLEnum(ItemType), nullable=False)
    record_type = Column(SQLEnum(RecordType), nullable=False)
    description = Column(String(255), nullable=False)
    brand = Column(String(50), nullable=True)
    color = Column(String(50), nullable=True)
    material = Column(String(50), nullable=True)
    image_url = Column(String(255), nullable=True)
    image_url_2 = Column(String(255), nullable=True)
    image_url_3 = Column(String(255), nullable=True)