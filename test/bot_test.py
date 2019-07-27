import unittest
import logging


class BotTest(unittest.TestCase):

    def test_roll(self):
        self.assertTrue(True)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO)

    unittest.main()
