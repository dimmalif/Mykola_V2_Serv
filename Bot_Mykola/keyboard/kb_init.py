from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Нульова сторінка

registration = KeyboardButton('Реєстрація👨🏼‍')
skip_reg = KeyboardButton('Пропустити')

null_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
null_keyboard.row(registration, skip_reg)

city_name = KeyboardButton('Відправити назву населеного пункту')
location = KeyboardButton('Відправити геолокацію')

# Перша сторінка
help_button = KeyboardButton('Допомога🆘')
all_func = KeyboardButton('Функції' + '🤖')
info_from_Mykola = KeyboardButton('Про Колю🚹')
report = KeyboardButton('Залишити відгук💭')

default_key_board_client = ReplyKeyboardMarkup(resize_keyboard=True)
default_key_board_client.add(all_func).row(help_button, info_from_Mykola).add(report)

# Друга сторінка
multimedia = KeyboardButton('Мультимедія📼')
rec_films = KeyboardButton('Рекомендація фільму🎬')
get_weather = KeyboardButton('Погода')
jock = KeyboardButton('Розваги🎭')
kurs = KeyboardButton('Курс валют💸')
back_to_start = KeyboardButton('🔣')

all_func_key_board_client = ReplyKeyboardMarkup(resize_keyboard=True)
all_func_key_board_client.row(multimedia, rec_films).row(get_weather, kurs).add(jock).row(back_to_start)

# Третя сторінка для мультимедії
search_music = KeyboardButton('Пошук музики для скачування🎼')
get_music = KeyboardButton('Завантаження музики📲')
convert = KeyboardButton('Конвертація відео в звук🛠')
back_to_all_func = KeyboardButton('◀️') # Назад


multimedia_func = ReplyKeyboardMarkup(resize_keyboard=True)
multimedia_func.row(search_music, get_music).add(convert).row(back_to_all_func, back_to_start)

# Третя сторінка для розваг
fackt = KeyboardButton('Цікавий факт⁉️')
alco_calendar = KeyboardButton('Яке сьогодні свято?🥳')


jock_func = ReplyKeyboardMarkup(resize_keyboard=True)
jock_func.row(fackt, alco_calendar).row(back_to_all_func, back_to_start)

text_all_func = 'Перелік того що Коля навчився робити'

text_multimedia = '->'
