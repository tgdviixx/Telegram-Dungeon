import re
import random
import logging
import unittest

'''
This file contains the logic for rolling a single die.

The roll function, by default, rolls a D20, returning 1-20.

Specifying a die with a different number of sides (more than 2) returns a
number between 0 and n+1, including numbers 1 to n. Unit tests provided.

See: https://docs.python.org/3.7/library/unittest.html
'''


d6_regex = re.compile(r'((d|D)(\d+))')


def roll(message):
    '''Given a message, returns tuple (Diesize, Result)'''
    logging.debug('Rolling die, input: ' + str(message))
    dice = d6_regex.findall(message)
    if message and dice:
        try:
            dietype = int(dice[0][2])
            logging.debug('Rolling a D' + str(dietype))
            if(dietype <= 1):
                raise ValueError('Die cannot be less than 2 sided.')
            result = random.randint(1, dietype)
            return (dietype, result)
        except ValueError:
            logging.error('Die input error.')
            return (None, None)
    else:
        result = random.randint(1, 20)
        return (20, result)


class TestRoll(unittest.TestCase):

    def test_roll(self):
        for x in range(100):
            self.assertTrue(roll('')[1] in range(21))

    def test_regex(self):
        self.assertEqual(roll('D10')[0], 10)
        self.assertEqual(roll('d45')[0], 45)
        self.assertEqual(roll('Roll a D13 bro D30')[0], 13)
        self.assertEqual(roll('d999')[0], 999)

    def test_regex_roll(self):
        for x in range(100):
            self.assertTrue(roll('D45')[1] in range(46))
        for x in range(100):
            self.assertTrue(roll('d6')[1] in range(7))


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(message)s',
        level=logging.INFO)

    unittest.main()
