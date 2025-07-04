from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    location: str
    userType: str
    mobileNumber: str
    nationalId: str
    is_active: bool = True
    police_station_id: int

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class PasswordChange(BaseModel):
    current_password: str
    new_password: str

class LoginRequest(BaseModel):
    username: str
    password: str