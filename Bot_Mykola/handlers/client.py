from pathlib import Path
# from aiogram import types
# from aiogram.dispatcher import Dispatcher
# from time import time, ctime


from Recognition.recognition import Recognition

from Bot_Mykola.SQLite.base import insert_blob
from Bot_Mykola.handlers.create_bot import bot
from Bot_Mykola.keyboard.body import *


async def take_audio(message: types.audio):
    username = message.from_user.username
    full_name = message.from_user.full_name
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    else:
        await message.reply("Формат документа не підтримується")
        return 0

    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = Path("", f"{username}.wav")

    await bot.download_file(file_path, destination=file_name)
    print('File')
    insert_blob(full_name, username, file_name)

    r = Recognition(file_name)
    await message.reply(r.recognise())

    print(f'Download new file at: {ctime(time())}')


def handler_registers_client(dp: Dispatcher):
    dp.register_message_handler(take_audio, content_types=types.ContentType.VOICE)
