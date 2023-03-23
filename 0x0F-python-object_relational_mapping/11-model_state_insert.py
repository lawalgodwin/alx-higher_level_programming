#!/usr/bin/python3

"""A script that adds a new state to the db"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import (Base, State)


if __name__ == '__main__':
    """Add new state to the db"""
    # create storage engine
    _, user, password, dbname = argv
    DB_URL = F'mysql+mysqldb://{user}:{password}@localhost/{dbname}'
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # migrate table(craete the table if not exist)
    Base.metadata.create_all(storage_engine)
    # create session to be used for DB transaction
    Session = sessionmaker(bind=storage_engine)
    # start talking to DB
    with Session() as session:
        Louisiana = State(name="Louisiana")
        session.add(Louisiana)
        session.commit()
        print(Louisiana.id)
