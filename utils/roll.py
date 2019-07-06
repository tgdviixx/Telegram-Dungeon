import re
import random
import logging

d6_regex = re.compile(r'((d|D)(\d+))')


def roll(message):
    '''Given a message, returns tuple (Diesize, Result)'''
    logging.info('Rolling die.')
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
