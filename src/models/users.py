from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from src.config.database import Base
from enum import Enum

class UserTypeEnum(str, Enum):
    SYSTEM_USER = "system_user"
    ADMIN = "admin"
    NORMAL_USER = "normal_user"

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
