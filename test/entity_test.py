import unittest
from src.entity import Entity


class EntityTest(unittest.TestCase):

    def test_init_character(self):
        mouse = Entity()
        self.assertEqual(mouse.health, 100)
