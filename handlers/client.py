from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_dp


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро Пожаловать', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с Ботом в Личку, напишите ему:\nhttps://t.me/home_263_bot')


# @dp.message_handler(commands=['Режим_Работы'])
async def home_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Каждый День с 7:00 до 00:00')


# @dp.message_handler(commands=['Расположение'])
async def home_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Страна Кырыгызстан ,Село - Ивановка ул.Токмаская 272')


@dp.message_handler(commands=['Меню'])
async def home_menu_command(message: types.Message):
    await sqlite_dp.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(home_open_command, commands=['Режим_Работы'])
    dp.register_message_handler(home_place_command, commands=['Расположение'])
    dp.register_message_handler(home_menu_command, commands=['Меню'])
