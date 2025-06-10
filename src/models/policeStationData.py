from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from src.config.database import Base
from enum import Enum

class PoliceStationType(str, Enum):
    POLICE_STATION = "police_station"
    POLICE_OFFICE = "police_office"

class PoliceStation(Base):
    __tablename__ = "police_stations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(15), nullable=False)
    email = Column(String(100), nullable=True)
    station_type = Column(SQLEnum(PoliceStationType), nullable=False)
    latitude = Column(String(20), nullable=True)
    longitude = Column(String(20), nullable=True)