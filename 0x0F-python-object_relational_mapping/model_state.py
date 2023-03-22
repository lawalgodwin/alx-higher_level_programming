#!usr/bin/python3

"""Mapping the `State` class to DB table `states`"""

from sqlalchemy.orm import (DeclarativeBase, mapped_column)
from sqlalchemy import (Integer, String)


class Base(DeclarativeBase):
    """Declarative Base class"""
    pass


class State(Base):
    """The class to be mapped to states table"""
    __tablename__ = 'states'

    id = mapped_column(Integer, primary_key=True)

    name = mapped_column(String(128), nullable=False)
