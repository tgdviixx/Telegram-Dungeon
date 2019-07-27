import re
import random
import logging

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
