from sqlalchemy.orm import Session
from src.models.users import User
from src.schemas.user import UserCreate
from src.auth.auth import get_password_hash, verify_password


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username,
                   first_name=user.first_name,
                   last_name=user.last_name,
                   location=user.location,
                   userType=user.userType,
                   mobileNumber=user.mobileNumber,
                   nationalId=user.nationalId,
                   email=user.email,
                   hashed_password=hashed_password,
                   is_active=user.is_active,
                   police_station_id=user.police_station_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def update_user_password(db: Session, user: User, new_password: str):
    user.hashed_password = get_password_hash(new_password)
    db.commit()
    db.refresh(user)
    return user