import logging
import unittest
import os
import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

'''
The Character class stores all information about player and non-player characters.
- PickleType: https://stackoverflow.com/a/1378818/9899022
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, PickleType, String 

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    properties = Column(PickleType)
    inventory = Column(PickleType)

    def __repr__(self):
        return "<User(name='%s', properties='%s', inventory='%s')>" % \
            (self.name, self.properties, self.inventory)


engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Base.metadata.create_all(engine)