#!/usr/bin/python3

"""script that prints the State object with
   the name passed as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import (Base, State)


if __name__ == '__main__':
    """Do not run when imported"""
    # create storage engine
    _, user, password, dbname, state = argv
    DB_URL = f"mysql+mysqldb://{user}:{password}@localhost/{dbname}"
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # create session to be used for quering db
    Session = sessionmaker(bind=storage_engine)

    # start querying
    with Session() as session:
        state = session.query(State).filter(State.name == state).first()
        if state:
            print(state.id)
        else:
            print("Nothing")
