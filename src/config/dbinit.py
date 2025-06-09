from src.config.database import Base, engine
from src.models.users import User

Base.metadata.create_all(bind=engine)