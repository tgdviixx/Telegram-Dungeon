import logging
import unittest

'''
The Character class stores all information about player and non-player characters.
'''

class Entity:
    '''Stores all information about a player character.'''

    # Class variables shared by all instances.

    def __init__(self):

        # Instance variables unique to each instance.
        self.health = 100
        self.stamina = 100


'''
Test class setup, inventory manipulation, attack and damage.
'''


class TestCharacter(unittest.TestCase):

    def test_init_entity(self):
        logging.info("Setting up an entity.")
        frog = Entity() 
        self.assertEqual(frog.health, 100)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO
    )
    unittest.main()
