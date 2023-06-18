#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).join(City).all()

    for i in res:
        print("{}: {}".format(i.id, i.name))
        for j in i.cities:
            print("    {}: {}".format(j.id, j.name))
