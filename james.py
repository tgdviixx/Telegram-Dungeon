from telegram.ext import Updater, CommandHandler
import random
import logging
import os
import re

'''
COMMANDS:
roll - Roll a die. Optionally specify a D-Type (D6, d8, d40)
set_role - Set user role.
hello - Test the bot.
'''

# Regex for all functions:
d6_regex = re.compile(r'((d|D)(\d+))')

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
    logging.debug('Got a HELLO command.')
    update.message.reply_text(
        'Hello, {}. I am JAMES, the Dungeon bot.\n\n{}'.format(
            update.message.from_user.first_name, str(
                update.message.from_user)))


def roll(bot, update):
    logging.debug('Got a ROLL command.')
    name = update.message.from_user.first_name
    dice = d6_regex.findall(update.message.text)
    if dice:
        try:
            dietype = int(dice[0][2])
            logging.debug('ROLLing a D' + str(dietype))
            num = random.randint(1, dietype)
            update.message.reply_text(
                '(D{}) {} rolled a {}'.format(
                    dietype, name, num))
        except ValueError:
            update.message.reply_text('Um, that isn\'t a die I know about.')

    else:
        num = random.randint(1, 20)
        update.message.reply_text('(D20) {} rolled a {}'.format(name, num))


def set_role(bot, update):
    logging.debug('Got a HELLO command.')
    update.message.reply_text(
        'Hello, {}.\n{}'.format(
            update.message.from_user.first_name, str(
                update.message.from_user)))


# Start the bot.
updater = Updater(os.getenv('JAMES_TELEGRAM'))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('roll', roll))
updater.dispatcher.add_handler(CommandHandler('set_role', set_role))

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
