from time import ctime, time
# from SQLite.sqlite import db_start, create_profile, edit_profile
from aiogram import types, Dispatcher
from Bot_Mykola.handlers.create_bot import dp
from .kb_init import *


@dp.message_handler(commands='start')
async def greeting(message: types.Message):
    await message.reply(f'Привіт, {message.from_user.full_name}, я голосовий помічник Микола, буду радий допомогти',
                        reply_markup=default_key_board_client)
    print(f'/start or /help : {ctime(time())}')


@dp.message_handler(text='Функції')
async def get_all_func_keyboard(message: types.Message):
    await message.answer('->', reply_markup=all_func_key_board_client)


@dp.message_handler(text='На початок')
async def back_to_start(message: types.Message):
    await message.answer('<-', reply_markup=default_key_board_client)


@dp.message_handler(text='Мультимедіа')
async def get_multimedia_func(message: types.Message):
    await message.answer('->', reply_markup=multimedia_func)


@dp.message_handler(text='Назад')
async def go_back(message: types.Message):
    await message.answer('<-', reply_markup=all_func_key_board_client)


@dp.message_handler(text='Головне меню')
async def back_in_all_func(message: types.Message):
    await message.answer('Початкова клавіатура', reply_markup=default_key_board_client)


# async def jocks(message: types.Message):
#     await message.reply('Розваги', reply_markup=jock_func)


