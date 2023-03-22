#!/usr/bin/python3

"""A script that fetches all states from the DB
   in an ascending order of state.id
"""

from sqlalchemy.orm import sessionmaker
from model_state import (Base, State)
from sqlalchemy import (create_engine, select)
from sys import argv

if __name__ == '__main__':
    """Get all states"""
    _, user, password, dbname = argv
    DB_URL = F"mysql+mysqldb://{user}:{password}@localhost/{dbname}"
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    Session = sessionmaker(bind=storage_engine)

    with Session() as session:
        states = session.query(State).order_by(State.id.asc())
        for state in states.all():
            print(F"{state.id}: {state.name}")
