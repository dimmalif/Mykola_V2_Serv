from pathlib import Path
from aiogram import types
from aiogram.dispatcher import Dispatcher
from time import time, ctime

from Recognition.recognizer import recognize

from Bot_Mykola.SQLite.base import edit_profile
from Bot_Mykola.handlers.create_bot import bot
from Bot_Mykola.keyboard.body import *


async def take_audio(message: types.audio):
    username = message.from_user.username
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    else:
        await message.reply("Формат документа не підтримується")
        return
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("", f"{file_id}.wav")
    await bot.download_file(file_path, destination=file_on_disk)
    await message.reply("Йде обробка...")
    # await edit_profile(username, file_on_disk)
    await message.reply(recognize(file_on_disk))
    print(f'Download new file at: {ctime(time())}')


# def get_name(message: types.message):
#     name = messa

def handler_registers_client(dp: Dispatcher):
    dp.register_message_handler(take_audio, content_types=types.ContentType.VOICE)
