#!/usr/bin/python3

"""A script that changes state name"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import (Base, State)


if __name__ == '__main__':
    """Update a state name"""
    # create storage engine
    _, user, password, dbname = argv
    DB_URL = f'mysql+mysqldb://{user}:{password}@localhost/{dbname}'
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # migrate tables
    Base.metadata.create_all(storage_engine)
    # create session for DB transactions
    Session = sessionmaker(bind=storage_engine)
    # start talking to db
    with Session() as session:
        # find the state to be updated
        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = "New Mexico"
            session.commit()
