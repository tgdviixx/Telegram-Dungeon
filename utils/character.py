import logging
import unittest

'''
The Character class stores all information about player and non-player characters.
'''


class Character:
    '''Stores all information about a player character.'''

    # Class variables shared by all instances.

    def __init__(self, identity, name):

        # Instance variables unique to each instance.
        self.inventory = {}
        self.realname = name
        self.charactername = name


'''
Test class setup, inventory manipulation, attack and damage.
'''


class TestCharacter(unittest.TestCase):

    def test_init_character(self):
        logging.info("Setting up a character.")
        max = Character('7850928375', 'Max')
        self.assertEqual(max.realname, 'Max')
        self.assertEqual(max.health, 100)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO
    )
    unittest.main()
