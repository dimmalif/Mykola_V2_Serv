from aiogram import types, Dispatcher
from aiogram.types import message
from moviepy.audio.io.AudioFileClip import AudioFileClip
from Skills.alco_calendar import get_holydays
from Bot_Mykola.SQLite.base import get_city
import Skills.movies
from Skills import movies, weather
from Skills.downloader import *
from Skills.exchange_rates import ExchangeRates
from Skills import facts


def recommended_film(text=None):
    movie = Skills.movies.Movies(text).get_film()
    result = f'Можете переглянути: {movie[0]}\nПосилання: {movie[1]}'
    print(result)
    return result


def download_one_music(text=None):
    downloader = Downloader(text)
    file_path = downloader.download()
    return file_path


# no callable voice
def converted_music(text=None):
    file_path = '/home/dmytro/Desktop/Mykola/Bot_Mykola'
    FILETOCONVERT = AudioFileClip(f"{file_path}/{text}.mp4")
    FILETOCONVERT.write_audiofile(f"{file_path}/{text}.mp3")
    FILETOCONVERT.close()
    return f"{file_path}/{text}"


def show_weather(text=None, user_id=None):

    try:
        city = get_city(user_id)
    except:
        return 'Ви не зареєстрували місто, тому ця функція недоступна. Напишіть в чат настуре повідомлення щоб зареєструвати:\n' \
               'Я проживаю в <Ваше місто в називному відмінку>'

    print(city)
    if not text:
        text = 'Коля яка погода'
    # print(text)

    result = ''
    w = weather.Weather(city=city, text_data=text)
    now = w.get_weather('now')
    f_day = w.get_weather('for day')

    result += w.formater(now) + '\n'
    result += 'Прогноз погоди на найближчий час'
    result += w.formater(f_day)

    return result


def exchange_rates(text=None):
    res = ExchangeRates().get_exchange_rates()
    return res


def give_holydays(text=None):
    return get_holydays()


def i_fact(text=None):
   return facts.fact()






