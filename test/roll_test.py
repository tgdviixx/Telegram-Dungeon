import unittest
import logging
from src.roll import roll

class RollTest(unittest.TestCase):

    def test_roll(self):
        for _ in range(100):
            self.assertTrue(roll('')[1] in range(21))

    def test_regex(self):
        self.assertEqual(roll('D10')[0], 10)
        self.assertEqual(roll('d45')[0], 45)
        self.assertEqual(roll('Roll a D13 bro D30')[0], 13)
        self.assertEqual(roll('d999')[0], 999)

    def test_regex_roll(self):
        for _ in range(100):
            self.assertTrue(roll('D45')[1] in range(46))
        for _ in range(100):
            self.assertTrue(roll('d6')[1] in range(7))


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO)

    unittest.main()