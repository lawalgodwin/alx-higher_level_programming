#!/usr/bin/python3

"""A script that fetches all states contating `a`"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import (Base, State)


if __name__ == '__main__':
    """Get all states containing `a`"""
    # create storage_engine
    _, user, password, dbname = argv
    DB_URL = F"mysql+mysqldb://{user}:{password}@localhost/{dbname}"
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # create DB seesion
    Session = sessionmaker(bind=storage_engine)
    # start querying
    with Session() as session:
        states = session.query(State).filter(State.name.like('%a%')).all()
        for state in states:
            print(F'{state.id}: {state.name}')
