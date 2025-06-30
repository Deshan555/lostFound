# class RecordType(str, Enum):
#     LOST = "lost"
#     FOUND = "found"
#
# class Pets(Base):
#     __tablename__ = "pets"
#
#     id = Column(Integer, primary_key=True, index=True)
#     record_type = Column(SQLEnum(RecordType), nullable=False)
#     name = Column(String(100), nullable=False)
#     description = Column(String(255), nullable=False)
#     pet_type = Column(String(50), nullable=False)
#     breed = Column(String(50), nullable=True)
#     color = Column(String(50), nullable=True)
#     age = Column(String(50), nullable=True)
#     image_url = Column(String(255), nullable=True)
#     image_url_2 = Column(String(255), nullable=True)
#     image_url_3 = Column(String(255), nullable=True)

from pydantic import BaseModel, EmailStr
from typing import Optional

class CreatePetRecordSchema(BaseModel):
    record_type: str
    name: str
    description: Optional[str] = None
    pet_type: str
    breed: Optional[str] = None
    color: Optional[str] = None
    age: Optional[str] = None
    image_url: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None