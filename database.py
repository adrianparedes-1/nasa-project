from sqlalchemy import create_engine
from . import models
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:password@localhost/nasa", echo=False)
# making session factory
SessionLocal = sessionmaker(engine)
models.Neo.metadata.create_all(engine) #create tables on db

def get_db():
    db = SessionLocal() #session instance
    try:
        yield db
    finally:
        db.flush()
        db.close()