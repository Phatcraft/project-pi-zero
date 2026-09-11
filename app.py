# Project Pi Zero Main App

from dotenv import dotenv_values
from libs.bot import TelegramBot

# Load Evironment variables
BOT_ID, BOT_HASH, BOT_TOKEN,\
SESSION_PATH, LOG_PATH, DATABASE_PATH = dotenv_values(".env").values()

# Create bot
bot = TelegramBot(BOT_ID, BOT_HASH, BOT_TOKEN, SESSION_PATH, LOG_PATH)
bot.start()