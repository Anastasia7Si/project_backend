from sqlalchemy import Column, Integer, String
from fastapi_users.db import SQLAlchemyBaseUserTable

from ..database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)


class UserApi(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
