import os
import re
from pathlib import Path
from aiogram.utils import exceptions
import aiogram

from loguru import logger
from Detectaig_command.detect_and_run import run
from Dataset import dataset
from Vectorizer.vector import *
from Skills.Functions import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from Recognition.recognition import Recognition
from Bot_Mykola.handlers.create_bot import bot
from Bot_Mykola.keyboard.body import *


async def take_audio(message: types.audio):
    username = message.from_user.username
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    else:
        await message.reply("Формат файлу не підтримується🙁")
        return 0

    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = Path("", f"{username}.wav")

    await bot.download_file(file_path, destination=file_name)
    print('File')

    r = Recognition(file_name)
    text = r.recognise()
    try:
        await message.reply(text)
    except aiogram.utils.exceptions.MessageTextIsEmpty:
        await message.reply('Ви відправили пусте повідомлення')

    parameters = vectoring(text)
    print(f'Download new file at: {ctime(time())}')
    result_func = eval(parameters[0] + '(text)')
    if '/home' in result_func:
        await message.reply_document(open(f'{result_func}', 'rb'))

    else:
        await message.reply(result_func)


def handler_registers_client(dp: Dispatcher):
    dp.register_message_handler(take_audio, content_types=types.ContentType.VOICE)
