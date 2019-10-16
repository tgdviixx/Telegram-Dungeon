import unittest
from src.database import connect


class RollTest(unittest.TestCase):

    def test_roll(self):
        self.assertTrue(connect())
