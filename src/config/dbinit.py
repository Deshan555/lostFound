from src.config.database import Base, engine
from src.models.users import User
from src.models.lostRecords import LostRecord
from src.models.electronicItems import ElectronicItem
from src.models.others import UndefinedLostItem
from src.models.jewelry import Jewelry
from src.models.wallet import Wallet
from src.models.document import Document
from src.models.policeStationData import PoliceStation
from src.models.findRecords import FindRecord

Base.metadata.create_all(bind=engine)