from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

load_dotenv()
bot = Bot(token=getenv('ВОТ_ТОКЕН'))
dp = Dispatcher(bot, storage=storage)
