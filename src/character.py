import logging
import unittest
import datetime
from src.entity import Entity

'''
The Character class stores all information about player and non-player characters.
'''


class Character(Entity):
    '''Stores all information about a player character.'''

    # Class variables shared by all instances.

    def __init__(self, identity, name):
        super().__init__()

        # Instance variables unique to each instance.

        self.realname = name
        self.charactername = name
        self.init_date = datetime.datetime.now()

        self.inventory = {}
        self.magicka = 10

