import unittest
import logging
from src.entity import Entity


class EntityTest(unittest.TestCase):

    def test_init_character(self):
        logging.info("Setting up a character.")
        mouse = Entity()
        self.assertEqual(mouse.health, 100)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO)

    unittest.main()
