"""Token bot"""

import os
import time
import logging

from dotenv import load_dotenv
from telebot import types, TeleBot
from telebot.types import Update

load_dotenv()

bot = TeleBot(os.getenv("API_TOKEN_ACCESS"))
