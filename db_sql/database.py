from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:dkflnfhfcjd2001@localhost/db_dealer'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
