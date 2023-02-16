import os
import re
from time import ctime, time
from Bot_Mykola.SQLite.base import *
from aiogram import types, Dispatcher, executor, Bot
from aiogram.dispatcher.storage import FSMContext
from Bot_Mykola.handlers.create_bot import dp, bot
from Vectorizer.vector import vectoring
from .kb_init import *
from Skills.movies import Movies
from aiogram.dispatcher import filters
from Bot_Mykola.handlers.client import take_audio
from Skills.Functions import *
from aiogram import types, Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup


class Storage_bot(StatesGroup):
    music_name = State()
    file = State()
    rep = State()


@dp.message_handler(commands='start')
async def greeting(message: types.Message):
    await message.answer_animation('https://i.gifer.com/G74b.gif')
    await create_profile(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.reply(
        f'Привіт, {message.from_user.full_name}, я голосовий помічник <b>Микола</b>, буду радий допомогти😁\n'
        'Для коректної роботи всіх функцій необхідно зареєструватись.\n'
        'Зробити це можна просто натиснувши на кнопку нище. Ви можете пропустити реєстрацію.',
        reply_markup=null_keyboard, parse_mode="HTML")
    print(f'/start or /help : {ctime(time())}')


@dp.message_handler(text='Реєстрація👨🏼‍')
async def reg(message: types.Message):
    await message.answer(
        '*Ви успішно зареєструвались!* Додайте дані про ваше місце знаходження і зможете слідкувати за '
        'погодою.\n'
        'Для цього напишіть в чат: "Я проживаю в  <_Ваше місто в називному відмінку_>"',
        reply_markup=default_key_board_client, parse_mode="Markdown")


@dp.message_handler(filters.Text(contains='Я проживаю', ignore_case=True))
async def reg_city(message: types.Message):
    res = re.findall(r'[яЯ] проживаю [ув] (.+)', message.text)
    print(res)
    add_city(message.from_user.id, res[0])
    await message.answer('Ви успішно оновили місце знаходження!🗺')


@dp.message_handler(text='Пропустити')
async def skip_reg(message: types.Message):
    await message.answer('Ви пропустили реєстрацію, деякі функції можуть бути *недоступні*. Приємного користування😊',
                         reply_markup=default_key_board_client, parse_mode="Markdown")


@dp.message_handler(text='Функції🤖')
async def get_all_func_keyboard(message: types.Message):
    await message.answer('Список доступних команд⬇️', reply_markup=all_func_key_board_client)
    await message.delete()


@dp.message_handler(text='Залишити відгук💭', state=None)
async def get_all_func_keyboard(message: types.Message):
    await message.answer('Залиште свій відгук нижче⬇️')
    await Storage_bot.rep.set()
    await message.delete()


@dp.message_handler(state=Storage_bot.rep)
async def download_music(message: types.Message, state: FSMContext):
    get_report(message.from_user.id, message.text)
    await message.answer('Команда розробки дякує за відгук😉')
    await state.finish()


@dp.message_handler(text='Допомога🆘')
async def back_to_start(message: types.Message):
    await message.answer(help_message(), parse_mode="HTML")
    await message.delete()


@dp.message_handler(text='🔣')
async def back_to_start(message: types.Message):
    await message.answer('Головне меню', reply_markup=default_key_board_client)
    await message.delete()


@dp.message_handler(text='Мультимедія📼')
async def get_multimedia_func(message: types.Message):
    await message.answer('Список доступних команд⬇️', reply_markup=multimedia_func)
    await message.delete()


@dp.message_handler(text='◀️')
async def go_back(message: types.Message):
    await message.answer('Назад', reply_markup=all_func_key_board_client)
    await message.delete()


@dp.message_handler(text='Розваги🎭')
async def jocks(message: types.Message):
    await message.reply('Список доступних команд⬇️', reply_markup=jock_func)
    await message.delete()


@dp.message_handler(text='Цікавий факт⁉️')
async def i_facts(message: types.Message):
    await message.reply(i_fact(), reply_markup=jock_func)
    await message.delete()


@dp.message_handler(text='Рекомендація фільму🎬')
async def film(message: types.Message):
    movie = Movies('коля перекомендуй фільм').get_film()
    await message.reply(f'*Можете переглянути:* {movie[0]}\n'
                        f'*Посилання:* {movie[1]}', parse_mode="Markdown")
    await message.delete()


@dp.message_handler(text='Погода🌤')
async def get_weather(message: types.Message):
    print('weather')
    await message.reply(show_weather(user_id=message.from_user.id), parse_mode="Markdown")
    await message.delete()


@dp.message_handler(text='Курс валют💸')
async def get_weather(message: types.Message):
    print('exchange_rates')
    await message.answer(exchange_rates(), parse_mode="Markdown")
    await message.delete()


@dp.message_handler(text='Яке сьогодні свято?🥳')
async def get_weather(message: types.Message):
    with open(f"{give_holydays()}", 'r', encoding='utf-8') as f:
        text = f.read()
    await message.answer(text)
    await message.delete()


@dp.message_handler(text='Завантаження вказаної пісні📲', state=None)
async def question_download_music(message: types.Message):
    await message.answer('Вкажіть повну назву бажаної пісні. Щоб відмінити команду напишіть *"Відміна"*',
                         parse_mode="Markdown")
    await Storage_bot.music_name.set()
    await message.delete()


@dp.message_handler(state=Storage_bot.music_name)
async def download_music(message: types.Message, state: FSMContext):
    print('start_download')
    if message.text.title() == 'Відміна':
        await message.answer('Відмінено')
        await state.finish()
        return 0

    await state.update_data(music_name=message.text)
    data = await state.get_data()
    result = download_one_music(text=f"Коля скачай пісню {data['music_name']}")
    await message.reply_document(open(f'{result}', 'rb'))
    await state.finish()
    # os.remove(result)
    print('removed')


@dp.message_handler(text='Конвертація відео (mp4) в звук (mp3) 🛠', state=None)
async def mp4_to_mp3(message: types.Message):
    await message.answer('Надішліть файл для обробки')
    await Storage_bot.file.set()
    await message.delete()


@dp.message_handler(content_types=["video"], state=Storage_bot.file)
async def download_music(message: types.Message, state: FSMContext):
    print('завантаження...')
    file_id = message.video.file_id  # Get file id
    file = await bot.get_file(file_id)  # Get file path
    await bot.download_file(file.file_path, f"{message.from_user.id}.mp4")
    res = converted_music(f"{message.from_user.id}")
    await message.reply_document(open(f'{res}.mp3', 'rb'))
    await state.finish()
    os.remove(f"{res}.mp4")
    os.remove(f"{res}.mp3")
    print('removed')
    await state.finish()


@dp.message_handler(state=Storage_bot.file)
async def check_type_file(message: types.Message, state: FSMContext):
    if message.content_type != 'video':
        await message.reply('Надіслано не відео')
        await state.finish()
