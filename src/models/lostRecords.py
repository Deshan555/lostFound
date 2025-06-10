from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.config.database import Base
from enum import Enum
from sqlalchemy.sql import func

class ItemTypeEnum(str, Enum):
    ELECTRONICS = "electronics"
    JEWELRY = "jewelry"
    DOCUMENT = "document"
    WALLET = "wallet"
    OTHERS = "undefined"

class RecordStatusEnum(str, Enum):
    OPEN = "open"
    MATCHED = "matched"
    RECOVERED = "recovered"


class LostRecord(Base):
    __tablename__ = "lost_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_type = Column(SQLEnum(ItemTypeEnum), nullable=False)
    description = Column(String(255), nullable=False)
    date_lost = Column(String(50), nullable=False)
    location_lost = Column(String(100), nullable=False)
    remarks = Column(String(255), nullable=True)
    reward = Column(String(50), nullable=True)
    subRecordID = Column(String(50), nullable=True)
    status = Column(SQLEnum(RecordStatusEnum), default=RecordStatusEnum.OPEN, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    electronicItems_ID = Column(Integer, ForeignKey('electronic_items.id'), nullable=True)
    jewelryItems_ID = Column(Integer, ForeignKey('jewelry_items.id'), nullable=True)
    document_ID = Column(Integer, ForeignKey('documents.id'), nullable=True)
    wallet_ID = Column(Integer, ForeignKey('wallets.id'), nullable=True)
    undefinedItems_ID = Column(Integer, ForeignKey('undefined_lost_items.id'), nullable=True)

    user = relationship("User", backref="lost_records")
    electronic_item = relationship("ElectronicItem", backref="lost_records")
    jewelry_item = relationship("JewelryItem", backref="lost_records")
    document = relationship("Document", backref="lost_records")
    wallet = relationship("Wallet", backref="lost_records")
    undefined_item = relationship("UndefinedLostItem", backref="lost_records")

