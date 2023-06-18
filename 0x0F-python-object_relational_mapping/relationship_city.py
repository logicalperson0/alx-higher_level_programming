#!/usr/bin/python3
"""
contains the class definition of a City and
an instance Base = declarative_base()
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()


class City(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True,
                nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
