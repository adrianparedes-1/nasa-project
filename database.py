from sqlalchemy import create_engine
from models import NeoMetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:password@localhost/nasa", echo=False)
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