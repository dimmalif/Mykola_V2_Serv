import re
from time import ctime, time
from Bot_Mykola.SQLite.base import *
from aiogram import types, Dispatcher
from Bot_Mykola.handlers.create_bot import dp, bot
from .kb_init import *
from Skills.movies import Movies
from aiogram.dispatcher import filters
from Bot_Mykola.handlers.client import take_audio
from Skills.Functions import *


@dp.message_handler(commands='start')
async def greeting(message: types.Message):
    await message.answer_animation('https://i.gifer.com/G74b.gif')
    await create_profile(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.reply(f'Привіт, {message.from_user.full_name}, я голосовий помічник Микола, буду радий допомогти😁\n'
                        'Для коректної роботи всіх функцій необхідно зареєструватись.\n'
                        'Зробити це можна просто натиснувши на кнопку нище.Ви можете пропустити реєстрацію.',
                        reply_markup=null_keyboard)
    print(f'/start or /help : {ctime(time())}')


@dp.message_handler(text='Реєстрація👨🏼‍')
async def reg(message: types.Message):
    await message.answer('Ви успішно зареєструвались! Додайте дані про ваше місце знаходження і зможете слідкувати за погодою.\n'
                         'Для цього напишіть в чат: Я проживаю в  <Ваше місто>', reply_markup=default_key_board_client)


@dp.message_handler(filters.Text(contains='Я проживаю', ignore_case=True))
async def reg_city(message: types.Message):
    res = re.findall(r'Я проживаю (\w\s\w+)', message.text)
    print(res)
    add_city(message.from_user.id, res[0])
    await message.answer('Ви успішно оновили місце знаходження!')


@dp.message_handler(text='Пропустити')
async def skip_reg(message: types.Message):
    await message.answer('Ви пропустили реєстрацію,деякі функції можуть бути недоступні.Приємного користування😊',
                         reply_markup=default_key_board_client)


@dp.message_handler(text='Функції🤖')
async def get_all_func_keyboard(message: types.Message):
    await message.answer('->', reply_markup=all_func_key_board_client)


@dp.message_handler(text='🔣')
async def back_to_start(message: types.Message):
    await message.answer('<-', reply_markup=default_key_board_client)


@dp.message_handler(text='Мультимедія📼')
async def get_multimedia_func(message: types.Message):
    await message.answer('Список доступних команд:⬇', reply_markup=multimedia_func)


@dp.message_handler(text='◀️')
async def go_back(message: types.Message):
    await message.answer('<-', reply_markup=all_func_key_board_client)


@dp.message_handler(text='Розваги🎭')
async def jocks(message: types.Message):
    await message.reply('Розваги🎭', reply_markup=jock_func)


@dp.message_handler(text='Рекомендація фільму🎬')
async def film(message: types.Message):
    movie = Movies('коля перекомендуй фільм').get_film()
    await message.reply(f'Можете переглянути: {movie[0]}\n'
                        f'Посилання: {movie[1]}')


@dp.message_handler(text='Погода')
async def get_weather(message: types.Message):
    print('weather')
    await message.reply(show_weather(user_id=message.from_user.id))


