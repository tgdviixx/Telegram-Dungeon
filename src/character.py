import logging
import unittest
import datetime

'''
The Character class stores all information about player and non-player characters.
'''


class Character:
    '''Stores all information about a player character.'''

    # Class variables shared by all instances.

    def __init__(self, identity, name):

        # Instance variables unique to each instance.

        self.realname = name
        self.charactername = name
        self.init_date = datetime.datetime.now()

        self.inventory = {}
        self.health = 100
        self.stamina = 100
        self.magicka = 10


'''
Test class setup, inventory manipulation, attack and damage.
'''


class TestCharacter(unittest.TestCase):

    def test_init_character(self):
        logging.info("Setting up a character.")
        maxine = Character('7850928375', 'Max')
        self.assertEqual(maxine.realname, 'Max')
        self.assertEqual(maxine.health, 100)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO
    )
    unittest.main()
