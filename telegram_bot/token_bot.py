"""Token bot"""

import os
import time

from dotenv import load_dotenv
from telebot import types, TeleBot

load_dotenv()

bot = TeleBot(os.getenv("API_TOKEN_ACCESS"))
