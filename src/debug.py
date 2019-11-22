import logging

'''
This file contains the logic for rolling a single die.

The roll function, by default, rolls a D20, returning 1-20.

Specifying a die with a different number of sides (more than 2) returns a
number between 0 and n+1, including numbers 1 to n. Unit tests provided.

See: https://docs.python.org/3.7/library/unittest.html
'''


def debug(bot, update):
    '''Given a message, returns tuple (Diesize, Result)'''
    logging.debug("Recieved debug query, returning user data.")


    has_character = False


    update.message.reply_text('''Hello, {}
User ID: {}
Character: {}''' .format(
    update.message.from_user.name,
    update.message.from_user.id,
    has_character
    ))
