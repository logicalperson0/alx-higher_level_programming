#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).all()

    for i in results:
        if 'a' in i.name:
            session.delete(i)

    session.commit()
