#!/usr/bin/python3

"""A script that fetches the first state in the db"""
from model_state import (Base, State)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    """Fetch the first state"""
    # provide the storage engine
    _, user, password, dbname = argv
    DB_URL = F"mysql+mysqldb://{user}:{password}@localhost/{dbname}"
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)

    # create session to be used for transaction
    Session = sessionmaker(bind=storage_engine)
    # query the db

    with Session() as session:
        state = session.query(State).order_by(State.id).all()[0]
        print(F"{state.id}: {state.name}")
