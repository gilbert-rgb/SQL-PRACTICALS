from sqlalchemy import Column,Integer,DateTime,String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    Username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    joined_on = Column(DateTime, default=datetime.utcnow)
