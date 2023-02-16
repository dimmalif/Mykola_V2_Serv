import flask
from aiogram.utils import executor
from handlers.client import *
# from handlers.create_bot import dp
from keyboard.body import *
from SQLite.base import db_start
# from keyboard.body import register_all_func_handler
from aiogram.utils.exceptions import NetworkError
handler_registers_client(dp)
# register_all_func_handler(dp)
from flask import Flask, request, Response
# app = Flask(__name__)

# @app.route('/',methods=['POST', 'GET'])
# def index():
#     # return '<h1>Привіт<h1>'
#     if request.headers.get('content-type') == 'application/json':
#         update = bot.types.Update.de_json(request.stream.read().decode('utf-8'))
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)
#
#     if request.method == 'POST':
#         return Response('ok', status=200)
#     else:
#         return ' '


async def on_start(_):
    print('Mykola is online')
    await db_start()


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_start, timeout=13000)
    except aiogram.utils.exceptions.NetworkError:
        print('ServerDisconnectedError: Server disconnected')
    except TimeoutError:
        print('Time out, process stop')

    # app.run()



