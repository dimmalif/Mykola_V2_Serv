from aiogram.utils import executor
from handlers.client import *
from handlers.create_bot import dp
from SQLite.sqlite import db_start
from keyboards.client_KB import register_all_func_handler

handler_registers_client(dp)
register_all_func_handler(dp)


async def on_start(_):
    print('Бот вийшов в он-лайн')
    await db_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
