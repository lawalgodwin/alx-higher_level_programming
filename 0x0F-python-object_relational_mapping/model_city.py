#!/usr/bin/python3
"""Maping City class to cities table"""
from model_state import Base
from sqlalchemy import (
                    Column,
                    Integer,
                    String,
                    ForeignKey)


class City(Base):
    """The city blueprint to be mapped"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
