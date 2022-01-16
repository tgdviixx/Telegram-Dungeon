import unittest
from src.database import Database


class RollTest(unittest.TestCase):

    def test_roll(self):
        mainbase = Database()
        self.assertTrue(mainbase.connect())
