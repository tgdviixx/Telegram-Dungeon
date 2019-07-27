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
        self.magicka = 0
