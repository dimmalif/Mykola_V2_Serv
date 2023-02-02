from pathlib import Path
from aiogram import types
from aiogram.dispatcher import Dispatcher
from time import time, ctime

from handlers.create_bot import bot
from keyboards.client_KB import *


async def take_audio(message: types.audio):
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    elif message.content_type == types.ContentType.AUDIO:
        file_id = message.audio.file_id
    else:
        await message.reply("Формат документа не підтримується")
        return
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("", f"{file_id}.wav")
    await bot.download_file(file_path, destination=file_on_disk)
    await message.reply("Аудіо отримано")
    print(f'Download new file at: {ctime(time())}')


def handler_registers_client(dp: Dispatcher):

    dp.register_message_handler(take_audio, content_types=[
        types.ContentType.VOICE,
        types.ContentType.AUDIO,
        types.ContentType.DOCUMENT
    ])
