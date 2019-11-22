import logging
import unittest
import os
import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

'''
The Character class stores all information about player and non-player characters.
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s', age='%i')>" % \
            (self.name, self.fullname, self.nickname, self.age)


engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Base.metadata.create_all(engine)