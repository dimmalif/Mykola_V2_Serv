from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

bot = Bot(token='6141163580:AAGLnjE_HvzCKNCbR065-gsPBjV1o9vfWrI')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)





@dp.message_handler(commands=['reg'])
async def user_register(message: types.Message):
    await message.answer("Введите своё имя")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Отлично! Теперь введите ваш адрес.")
    await UserState.next()  # либо же UserState.adress.set()


@dp.message_handler(state=UserState.address)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(f"Имя: {data['username']}\n"
                         f"Адрес: {data['address']}")

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)