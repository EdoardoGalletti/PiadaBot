"""
Very stupid bot to indicate the quantities of ingredients to prepare the desired number of piadines

Mother"s recipe for 16 piadine:
	FLOUR: 	700g
	LARD:	100g
	MILK:	175g
	WATER:	175g
	SWEETS YEAST:	15g
	SALT: 	q.s.
	HONEY:	q.s.
"""

class Ingredient:
	def __init__(self, name, quantity):
		self.name = name
		self.quantity = quantity

wheat = Ingredient("Farina", 700/16)
lard = Ingredient("Strutto", 100/16)
milk = Ingredient("Latte", 175/16)
water = Ingredient("Farina", 175/16)
yeast = Ingredient("Lievito per dolci non vanigliato", 15/16)

import logging
import telegram
import telepot
import urllib3
import math

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

updater = Updater(token="751566911:AAHUJoC-mZAPEVA8u8xmP2BM7gO-lmP2O54")
dispatcher = updater.dispatcher

# Command handlers (they usually take the two arguments bot and update)

def start(bot, update):
	"""Send a message when the command /start is issued"""
	bot.send_message(chat_id=update.message.chat_id, text="I'm the PiadaBot! Quante piadine vuoi fare?\nScrivi: \"/piade x\", dove x è il numero di piadine desiderato.")

#########################################crap
def echo(update, context):
   """Echo the user message."""
   update.message.reply_text(update.message.text)

#########################################crap
def caps(bot, update, args):
   """Echo the user message, but in CAPS."""
   text_caps = " ".join(args).upper()
   bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def piade(bot, update, args):
	"""Set the amount of piadine to eat and get the quantities of ingredients"""
	# user_says = " ".join(args)
	piade = float(args[0])
	message =\
	"*" + wheat.name + "*: " + str(int(wheat.quantity*piade)) + "g \n" +\
	"*" + lard.name + "*: " + str(int(lard.quantity*piade)) + "g \n" +\
	"*" + milk.name + "*: " + str(int(milk.quantity*piade)) + "g \n" +\
	"*" + water.name + "*: " + str(int(water.quantity*piade)) + "g \n" +\
	"*" + yeast.name + "*: " + str(math.ceil(yeast.quantity*piade)) + "g \n" +\
	"*Sale*: q.b.\n*Miele*: q.b." 
	bot.send_message(chat_id=update.message.chat_id, text = message, parse_mode = telegram.ParseMode.MARKDOWN) 


def unknown(bot, update):
   """Message sent when an un unrecognized command is sent"""
   bot.send_message(chat_id=update.message.chat_id, text="No compriendo nu caz.")


def main():
   """Start the bot """
   # Create the Updater and pass it your bot"s token.
   updater = Updater(token="751566911:AAHUJoC-mZAPEVA8u8xmP2BM7gO-lmP2O54")
   # Get the dispatcher to register handlers
   dispatcher = updater.dispatcher

   # on different commands - answer in Telegram
   dispatcher.add_handler(CommandHandler("start", start))
   dispatcher.add_handler(CommandHandler("caps", caps, pass_args=True))
   dispatcher.add_handler(CommandHandler("piade", piade, pass_args=True))

   # on unknown command - show message in Telegram
   dispatcher.add_handler(MessageHandler(Filters.command, unknown))

   # Start the Bot
   updater.start_polling()
   updater.idle()

if __name__ == "__main__":
   main()

