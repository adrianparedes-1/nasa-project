from sqlalchemy import create_engine
from models import NeoMetaData
import os
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
db_uri = os.getenv("DATABASE_URI")
engine = create_engine(db_uri, echo=False)

# making session factory
SessionLocal = sessionmaker(engine)
NeoMetaData.metadata.create_all(engine) #create tables on db

def get_db():
    db = SessionLocal() #session instance
    try:
        yield db
    finally:
        db.flush()
        db.close()