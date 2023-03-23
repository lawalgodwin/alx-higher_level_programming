#!/usr/bin/python3

"""A script that prints all City objects from
   the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import (Base, State)
from model_city import (City)


if __name__ == '__main__':
    """Print all cities in the DB"""
    # create storage engine
    _, user, password, dbname = argv
    DB_URL = f'mysql+mysqldb://{user}:{password}@localhost/{dbname}'
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # Migrate(update) the DB
    Base.metadata.create_all(storage_engine)
    # create session for db interactions
    Session = sessionmaker(bind=storage_engine)
    # start interacting with DB
    with Session() as session:
        rows = session.query(City, State).join(State).all()
        for city, state in rows:
            print(f'{state.name}: ({city.id}) {city.name}')
