import os

from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(token='6104493412:AAH4yGpullDbjS3CelBmNh-KhiALV_prsiQ')
dp = Dispatcher(bot)

