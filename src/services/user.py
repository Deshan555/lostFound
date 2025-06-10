from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.schemas.user import UserCreate, UserOut, Token, PasswordChange
from src.actions.user_actions import create_user, get_user_by_username, update_user_password
from src.auth.auth import verify_password, create_access_token, get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.put("/password", response_model=UserOut)
def change_password(
    password_data: PasswordChange,
    username: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password_data.current_password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid current password")
    return update_user_password(db, user, password_data.new_password)

@router.get("/me", response_model=UserOut)
def get_user_details(username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/me", response_model=UserOut)
def update_user_details(
    email: str,
    username: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.email = email
    db.commit()
    db.refresh(user)
    return user