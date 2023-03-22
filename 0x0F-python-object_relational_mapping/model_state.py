#!usr/bin/python3

"""Mapping the `State` class to DB table `states`"""

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import (Integer, String, Column)


Base = declarative_base()

class State(Base):
    """The class to be mapped to states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)
