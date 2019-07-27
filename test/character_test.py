import unittest
import logging
from src.character import Character


class CharacterTest(unittest.TestCase):

    def test_init_character(self):
        logging.info("Setting up a character.")
        maxine = Character('7850928375', 'Max')
        self.assertEqual(maxine.realname, 'Max')
        self.assertEqual(maxine.health, 100)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO)

    unittest.main()
