import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import markup2 as nav
import teleScript as script
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

class STG(StatesGroup):
    items = State()
    letter = State()
    place = State()
    letters = State()
    function = State()

bot = Bot(token =config.TOKEN)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)


    text = message.from_user.full_name
    await bot.send_message(message.from_user.id, text)

@dp.message_handler(commands=['Начать новое слово'], state=None)
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новое слово', reply_markup = nav.functionMenu)

@dp.message_handler(commands=['Главное меню'], state=None)
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)