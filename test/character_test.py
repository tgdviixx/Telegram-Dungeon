import unittest
from src.character import Character


class CharacterTest(unittest.TestCase):

    def test_init_character(self):
        maxine = Character('7850928375', 'Max')
        self.assertEqual(maxine.realname, 'Max')
        self.assertEqual(maxine.health, 100)
