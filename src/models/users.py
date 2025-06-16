from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey
from src.config.database import Base
from enum import Enum

from src.models.policeStationData import PoliceStation

class UserTypeEnum(str, Enum):
    SYSTEM_USER = "system_user"
    ADMIN = "admin"
    NORMAL_USER = "normal_user"
    POLICE_STATION_OFFICER = "police_station_officer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    location = Column(String(100), index=True)
    userType = Column(SQLEnum(UserTypeEnum), index=True)  # Note the alias here
    mobileNumber = Column(String(15), unique=True, index=True)
    nationalId = Column(String(20), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Integer, default=1)
    police_station_id = Column(Integer, nullable=True)

    police_station = Column(Integer, ForeignKey('police_stations.id'), nullable=True)
