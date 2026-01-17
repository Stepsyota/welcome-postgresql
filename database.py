from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#"postgresql://user:password@postgresserver/db"
DATABASE_URL = "postgresql://user:password@localhost:5542/db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Connection succesful!")
except Exception as e:
    print(f"Error connection: {e}")

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)