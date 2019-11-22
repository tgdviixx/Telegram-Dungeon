import os
import sys
import unittest

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.character import Character

engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Session = sessionmaker(bind=engine)

class CharacterTest(unittest.TestCase):


    def test_1_init_character(self):
        
        testothy = Character(name='test', fullname='testothy jones',
                             nickname='testy', age=19)

        self.assertEqual(testothy.name, 'test')


    def test_2_add_character_to_db(self):
        
        session = Session()

        testothy = Character(name='test', fullname='testothy jones',
                             nickname='testy', age=19)
        
        session.add(testothy)
        session.commit()

        session.close()

        self.assertEqual(True, True)
