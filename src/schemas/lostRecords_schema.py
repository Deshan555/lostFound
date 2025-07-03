from pydantic import BaseModel, constr
from typing import Optional, Union, List
from datetime import datetime

from src.schemas.jewelry_schema import CreateJewelrySchema
from src.schemas.documents_schema import createDocumentSchema
from src.schemas.wallets_schema import CreateWalletSchema
from src.schemas.electronics_schema import CreateElectronicItemSchema
from src.schemas.others_schema import CreateUndefinedLostItemSchema
from src.schemas.petRecords_schema import CreatePetRecordSchema

# class CreateLostRecordSchema(BaseModel):
#     user_id: int
#     item_type: str
#     description: str
#     date_lost: str
#     location_lost: str
#     remarks: Optional[str] = None
#     reward: Optional[str] = None
#     subRecordID: Optional[str] = None
#     status: str = "open"
#     created_at: Optional[datetime] = None
#     electronicItems_ID: Optional[int] = None
#     jewelryItems_ID: Optional[int] = None
#     document_ID: Optional[int] = None
#     wallet_ID: Optional[int] = None
#     undefinedItems_ID: Optional[int] = None
#     sub_record: {
#         CreateWalletSchema ||
#         CreateJewelrySchema ||
#         createDocumentSchema ||
#         CreateElectronicItemSchema ||
#         CreateUndefinedLostItemSchema
#     } = None


class CreateLostRecordSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    item_type: constr(max_length=50)
    description: constr(max_length=255)
    date_lost: str
    location_lost: constr(max_length=255)
    reward: Optional[constr(max_length=255)] = None
    subRecordID: Optional[constr(max_length=50)] = None
    status: constr(max_length=50) = "open"
    created_at: Optional[datetime] = None
    cover_image_url: Optional[str] = None
    electronicItems_ID: Optional[int] = None
    jewelryItems_ID: Optional[int] = None
    document_ID: Optional[int] = None
    wallet_ID: Optional[int] = None
    undefinedItems_ID: Optional[int] = None
    pets_ID: Optional[int] = None
    # sub_record: Optional[Union[
    #     CreateWalletSchema,
    #     CreateJewelrySchema,
    #     createDocumentSchema,
    #     CreateElectronicItemSchema,
    #     CreateUndefinedLostItemSchema,
    #     CreatePetRecordSchema
    # ]] = None

    class Config:
        orm_mode = True

class UpdateLostRecordSchemaByID(BaseModel):
    item_type: Optional[str] = None
    description: Optional[str] = None
    date_lost: Optional[str] = None
    location_lost: Optional[str] = None
    remarks: Optional[str] = None
    reward: Optional[str] = None
    subRecordID: Optional[str] = None
    status: Optional[str] = "open"
    created_at: Optional[datetime] = None
    electronicItems_ID: Optional[int] = None
    jewelryItems_ID: Optional[int] = None
    document_ID: Optional[int] = None
    wallet_ID: Optional[int] = None
    undefinedItems_ID: Optional[int] = None

    class Config:
        orm_mode = True


