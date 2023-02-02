from time import ctime, time
from SQLite.sqlite import db_start, create_profile, edit_profile
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types.message import *

help_buttonn = KeyboardButton('/Допомога')
all_func_Mykola = KeyboardButton('/Всі_функції')

default_key_board_client = ReplyKeyboardMarkup(resize_keyboard=True)
default_key_board_client.row(all_func_Mykola).row(help_buttonn)

multimedia = KeyboardButton('/Мультимедіа')
microcontroller_comands = KeyboardButton('/Робота_з_розумним_будинком')
other = KeyboardButton('/Інше')
back_in_start = KeyboardButton('/На_початок')

all_func_key_board_client = ReplyKeyboardMarkup(resize_keyboard=True)
all_func_key_board_client.row(multimedia, microcontroller_comands).add(other).add(back_in_start)

recomendet_films = KeyboardButton('/Рекомендація_фільму')
get_music = KeyboardButton('/Завантаження_музики')
back_to_all_func = KeyboardButton('/Всі_функції')

multimedia_func = ReplyKeyboardMarkup(resize_keyboard=True)
multimedia_func.row(recomendet_films, get_music).row(back_to_all_func, back_in_start)

alco_calendar = KeyboardButton('/Календар_алкоголіка')
take_weather = KeyboardButton('/Погода')

other_func = ReplyKeyboardMarkup(resize_keyboard=True)
other_func.row(alco_calendar, take_weather).row(back_to_all_func, back_in_start)

text_all_func = 'Мультимедіа (завантаження або пошук музики, рекомендація фільмів)\n' \
                'Робота з розумним будинком\n' \
                'Інше\n'

text_multimedia = 'Рекомендація фільмів\nПошук музики, її завантаження і т.п.'

text_other_func = 'Календар алкоголіка(свят)\nПогода'


async def get_all_func_keyboard(message: types.message):
    await message.answer(text_all_func, reply_markup=all_func_key_board_client)


async def back_in_start(message: types.Message):
    await message.answer('Перехід на початкову клавіатуру', reply_markup=default_key_board_client)


async def get_multimedia_func(message: types.Message):
    await message.answer(text_multimedia, reply_markup=multimedia_func)


async def get_other_func(message: types.Message):
    await message.answer(text_other_func, reply_markup=other_func)


async def back_in_all_func(message: types.Message):
    await message.answer('Перехід на минулу клавіатуру', reply_markup=all_func_key_board_client)


async def send_welcome(message: types.Message):
    func = 'Ви завжди можете відправити бажану голосову команду.На даний момент аудіофайл лише завантажується на сервер'
    await message.reply(f"Привіт!Це тестова версія голосового помічника 'Микола'\n"
                        f"На разі реалізовано:\n {func} ", reply_markup=default_key_board_client)

    await create_profile(user_id=message.from_user.username)
    # with open('users.txt', 'a+', encoding='utf-8') as file:
    #     file.write('\n' + user[0])

    print(f'/start or /help : {ctime(time())}')


def register_all_func_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'Допомога'])
    dp.register_message_handler(get_all_func_keyboard, commands='Всі_функції')
    dp.register_message_handler(back_in_start, commands='На_початок')
    dp.register_message_handler(get_multimedia_func, commands='Мультимедіа')
    dp.register_message_handler(get_other_func, commands='Інше')
    dp.register_message_handler(back_in_all_func, commands='Всі_функції')
