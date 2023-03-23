#!/usr/bin/python3

"""A script that deletes all State objects with
   a name containing the letter a from the
   database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import (Base, State)


if __name__ == '__main__':
    """Only delete states containing `a`"""
    # create storage_engine
    _, user, password, dbname = argv
    DB_URL = f'mysql+mysqldb://{user}:{password}@localhost/{dbname}'
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # Migrate or Update the Database with tables
    Base.metadata.create_all(storage_engine)
    # create session for db transactions
    Session = sessionmaker(bind=storage_engine)
    # start interacting with db
    with Session() as session:
        states = session.query(State).filter(State.name.like('%a%')).all()
        if states:
            for s in states:
                session.delete(s)
            session.commit()
