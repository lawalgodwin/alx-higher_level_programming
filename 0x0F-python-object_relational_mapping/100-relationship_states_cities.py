#!/usr/bin/python3

"""A script that creates the State “California” with
   the City “San Francisco” from the
   database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import (Base, State)
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    """Create a state and a state city at the same time"""
    # create storage engine
    _, user, password, dbname = argv
    DB_URL = f'mysql+mysqldb://{user}:{password}@localhost/{dbname}'
    storage_engine = create_engine(DB_URL, pool_pre_ping=True)
    # Migrate DB
    Base.metadata.create_all(storage_engine)
    # create session for db interactions
    Session = sessionmaker(bind=storage_engine)
    # start interactions
    session = Session()
    try:
        california = State(name="California")
        new_city = City(name="San Francisco")
        california.cities.append(new_city)
        session.add(california)
        session.commit()
    except Exception as e:
        print("Error occured: ", e)
