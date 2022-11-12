#!/usr/bin/python3
"""
Start link class to table in database with sqlalchemy
Script that prints the `State` Object with the 'name' passed
as argument in command line.
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for wanted_id in session.query(State).filter(State.name == sys.argv[4]):
        if wanted_id:
            found = True
            print("{:d}".format(wanted_id.id))
    if found is False:
        print("Not found")
    session.close()
