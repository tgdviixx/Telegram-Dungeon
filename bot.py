from telegram.ext import Updater, CommandHandler
from pprint import pprint
import random
import logging
import os
import re

# Get Utils.
from src.roll import roll
from src.character import Character

'''
COMMANDS:
roll - Roll a die. Optionally specify a D-Type (D6, d8, d40)
set_role - Set user role.
hello - Test the bot.
'''

# Regex for all functions:
d6_regex = re.compile(r'((d|D)(\d+))')

# Pre-database development, store character info in memory.
characters = {}

# Set debugging level based on environment.
if os.getenv('DYNO'):
    logging.basicConfig(
        format='%(levelname)s - %(message)s',
        level=logging.INFO)
else:
    logging.basicConfig(
        format='%(asctime)s %(levelname)s:  %(name)s - %(message)s',
        level=logging.DEBUG)


def hello(bot, update):
    logging.info('Got a HELLO command.')
    bot.send_message(chat_id=update.message.chat_id,
                     text='Hello, {}. I am JAMES, the Dungeon bot.\n\n{}'.format(
                         update.message.from_user.first_name, str(
                             update.message.from_user)))


def action_roll_die(bot, update):
    logging.info('Got a ROLL command.')
    result = roll(update.message.text)
    if(result[0]):
        bot.send_message(
            chat_id=update.message.chat_id,
            text='(D{}) {} rolled {}'.format(
                result[0],
                update.message.from_user.first_name,
                result[1]))
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text='The die fell off the table.')


def action_set_role(bot, update):
    logging.info('Got a SET-ROLE command.')


def action_debug(bot, update):
    logging.info('Got a DEBUG command.')
    print("\n\nBOT:")
    pprint(bot)
    print("\n\nUPDATE:")
    pprint(update)
    pprint(update)
    print("\n\n")


def main():
    '''Start the bot.'''
    updater = Updater(os.getenv('JAMES_TELEGRAM'))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('roll', action_roll_die))
    updater.dispatcher.add_handler(CommandHandler('set_role', action_set_role))
    updater.dispatcher.add_handler(CommandHandler('debug', action_debug))

    logging.info('Starting JAMES bot.')
    if os.getenv('DYNO'):
        logging.info('Heroku container detected, using WEBHOOKS.')
        PORT = int(os.environ.get("PORT", "8443"))
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=os.getenv('JAMES_TELEGRAM'))
        updater.bot.set_webhook(
            "https://telegram-james.herokuapp.com/{}".format(os.getenv('JAMES_TELEGRAM')))
        updater.idle()
    else:
        logging.info('Local env detected, using POLLING.')
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    main()
