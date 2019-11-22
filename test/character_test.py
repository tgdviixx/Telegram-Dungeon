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

    def test_0_clear_database(self):
        session = Session()

        for user in session.query(Character).filter_by(name='Testothy Jones'):
            session.delete(user)

        session.commit()
        session.close()

    def test_1_init_character(self):

        testothy = Character(id=123, name="Testothy Jones",
                             properties={}, inventory={})

        self.assertEqual(testothy.name, 'Testothy Jones')

    def test_2_add_character_to_db(self):

        session = Session()
        
        testothy = Character(id=123, name="Testothy Jones",
                             properties={}, inventory={})

        session.add(testothy)
        session.commit()

        session.close()

    def test_3_check_if_testothy_in_db(self):
        session = Session()

        copy = session.query(Character).filter_by(name="Testothy Jones").first()
        self.assertEqual(copy.id, 123)

        session.close()

    def test_4_attempt_to_create_duplicate_testothy(self):
        session = Session()

        with self.assertRaises(Exception):
            testothy = Character(id=123, name="Testothy Jones",
                             properties={}, inventory={})

            session.add(testothy)
            session.commit()

        session.close()