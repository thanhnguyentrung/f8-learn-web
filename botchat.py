# Import the necessary libraries
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


# Set the OpenAI API key
openai.api_key = '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'

# Set the Telegram bot token
bot_token = '6129452848:AAGic9N4Wf9zr4lP2rkoNaAWU8UW4uZUn1o'

# Create the Telegram bot
bot = telegram.Bot(token=bot_token)

# Define the /start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am Smart AIShiba!")

# Define the /help command handler
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="To use me, simply send me a message!")
