import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Class that can Mapped object to database
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=False)