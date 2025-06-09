from sqlalchemy import text
from src.config.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connected:", result.scalar() == 1)
except Exception as e:
    print("Database connection failed:", e)