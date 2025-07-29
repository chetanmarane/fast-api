from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Set your own connection string
username = os.getenv("POSTGRESQL_USERNAME")
password = os.getenv("POSTGRESQL_PASSWORD")      
host= os.getenv("POSTGRESQL_SERVER")
port= os.getenv("POSTGRESQL_PORT")
database= os.getenv("POSTGRESQL_DATABASE")
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:959696@localhost:5432/mydb"
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()