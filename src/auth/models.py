from datetime import datetime
from sqlalchemy import (TIMESTAMP, Column, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from fastapi_users.db import SQLAlchemyBaseUserTable

from ..database import Base




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)



class UserApi(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)


