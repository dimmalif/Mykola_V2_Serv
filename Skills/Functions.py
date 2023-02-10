from aiogram import types, Dispatcher
from aiogram.types import message
from Bot_Mykola.SQLite.base import get_city


import Skills.movies
from Skills import movies, weather
from Skills.downloader_music.download_music import *


def recommended_film(text=None):
    movie = Skills.movies.Movies(text).get_film()
    result = f'Можете переглянути: {movie[0]}\nПосилання: {movie[1]}'
    print(result)
    return result


def download_one_music(text=None):
    downloader = Downloader_music(text)
    path_file = downloader.download__first_music()
    return path_file


def show_weather(text=None, user_id=None):
    try:
        city = get_city(user_id)
    except:
        return 'Ви не зареєстрували місто, тому ця функція недоступна.Напишіть в чат наступре повідомлення щоб зареєструвати:\n' \
               'Я проживаю в <Ваше місто>'
    # if not text:
    #     text = 'Коля яка погода'
    # print(text)
    print(city)

    result = ''
    w = weather.Weather(city='Київ', text_data=text)
    now = w.get_weather('now')
    f_day = w.get_weather('for day')

    result += w.formater(now) + '\n'
    result += w.formater(f_day)

    return result



