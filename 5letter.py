import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import markup as nav
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

letter = 0
place = 0

'''user'''




@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)


    text = message.from_user.full_name
    await bot.send_message(message.from_user.id, text)

    #items = script.start()
    #await bot.send_message(message.from_user.id, items)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Начать новое слово':
        #new_word()
        await bot.send_message(message.from_user.id, 'Новое слово', reply_markup = nav.functionMenu)

        items = script.start()
        await bot.send_message(message.from_user.id, items)

    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)

    elif message.text == 'Инфо':
        await bot.send_message(message.from_user.id, 'Бот для помощи в игре "5БУКВ". \nДля старт введите в самой игре любое подходящее слово, а затем начните использовать подсказки бота во вкладке "Новое слово"')
    
    elif message.text == 'Знаю желтую букву':
        await bot.send_message(message.from_user.id, 'Введите букву')
        
    #elif message.text == 'Знаю серую букву':

    elif message.text == 'Знаю белую букву':
        await message.answer('Выберите букву', reply_markup=nav.lettersMenu)
        await message.answer('Выберите место', reply_markup=nav.placeMenu)
        await message.answer('Просеять', reply_markup=nav.cMenu)
        #items = script.start()
        letter=white1()
        place=white2()
        white3()
        


        
def white1()->letter:
    @dp.callback_query_handler(Text(startswith='letter_'))
    async def func(callback: types.CallbackQuery)->letter:
        letter = callback.data[7]
        await callback.message.answer(letter)

def white2()->place:
    @dp.callback_query_handler(Text(startswith='pl_'))
    async def func(callback: types.CallbackQuery)->place:
        place = callback.data[3]
        await callback.message.answer(place)

def white3():   
    @dp.callback_query_handler(Text(startswith='cycle'))
    async def func(callback: types.CallbackQuery):
         await callback.message.answer(letter)
         await callback.message.answer(place)


     
####admin

####back


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)