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

"""@dp.message_handler(state=None)
async def bot_message(message: types.Message):
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)

    elif message.text == 'Инфо':
        await bot.send_message(message.from_user.id, 'Бот для помощи в игре "5БУКВ". \nДля старт введите в самой игре любое подходящее слово, а затем начните использовать подсказки бота во вкладке "Новое слово"')
"""
@dp.message_handler(Text(startswith='Начать'),state=None)
async def bot_message(message: types.Message):
    #elif message.text == 'Начать новое слово':
    await bot.send_message(message.from_user.id, 'Новое слово', reply_markup = nav.functionMenu)

    items = script.start()
    
        #file1 = open('words.txt', 'a')
        #file1.write(items)
        #file1.close()

    #await STG.function.set()
    await fun1(items)

async def fun1(items):
    await STG.function.set()
    @dp.message_handler(Text(startswith='Знаю'),state=STG.function)
    async def func_ans(message:types.message, state: FSMContext):
        function = message.text
        async with state.proxy() as data:
            data['function']=function

        data = await state.get_data()

        await bot.send_message(message.from_user.id, 'Ты тут')
        await bot.send_message(message.from_user.id, data['function'])
        #await state.finish()
        
        if data['function'] == 'Знаю желтую букву':
            await bot.send_message(message.from_user.id, 'Введите букву')
            await STG.letter.set()

            @dp.message_handler(state=STG.letter)
            async def ans_let(message:types.message, state: FSMContext):
                letter = message.text
                async with state.proxy() as data:
                    data['letter']=letter

                data = await state.get_data()
                await bot.send_message(message.from_user.id, 'Ты тут1')
                await bot.send_message(message.from_user.id, data['letter'])
                await bot.send_message(message.from_user.id, 'Введите номер буквы')
                await STG.place.set()

            @dp.message_handler(state=STG.place)
            async def ans_plc(message:types.message, state: FSMContext):
                place = message.text
                async with state.proxy() as data:
                    data['place']=place

                data = await state.get_data()
                await bot.send_message(message.from_user.id, data['place'])

                #items = script.yellow(items, data['letter'], data['place'])

                await bot.send_message(message.from_user.id, script.yellow(items, data['letter'], int(data['place'])))
                await state.reset_state()
                #await state.finish()
                await fun1(items)

        if data['function'] == 'Знаю белую букву':
            await bot.send_message(message.from_user.id, 'Введите букву')
            await STG.letter.set()

            @dp.message_handler(state=STG.letter)
            async def ans_let(message:types.message, state: FSMContext):
                letter = message.text
                async with state.proxy() as data:
                    data['letter']=letter

                data = await state.get_data()
                await bot.send_message(message.from_user.id, 'Ты тут1')
                await bot.send_message(message.from_user.id, data['letter'])
                await bot.send_message(message.from_user.id, 'Введите номер буквы')
                await STG.place.set()

            @dp.message_handler(state=STG.place)
            async def ans_plc(message:types.message, state: FSMContext):
                place = message.text
                async with state.proxy() as data:
                    data['place']=place

                data = await state.get_data()
                await bot.send_message(message.from_user.id, data['place'])

                #items = script.yellow(items, data['letter'], data['place'])

                await bot.send_message(message.from_user.id, script.white(items, data['letter'], int(data['place'])))
                await state.reset_state()
                #await state.finish()
                await fun1(items)

        if data['function'] == 'Знаю серую букву':
            await bot.send_message(message.from_user.id, 'Введите букву')
            await STG.letter.set()

            @dp.message_handler(state=STG.letter)
            async def ans_let(message:types.message, state: FSMContext):
                letter = message.text
                async with state.proxy() as data:
                    data['letter']=letter

                data = await state.get_data()
                await bot.send_message(message.from_user.id, 'Ты тут1')
                await bot.send_message(message.from_user.id, data['letter'])
                await bot.send_message(message.from_user.id, script.grey(items, data['letter']))
                await state.reset_state()
                await fun1(items)

        if data['function'] == 'Знаю серые буквы':
            await bot.send_message(message.from_user.id, 'Введите буквы через пробел')
            await STG.letters.set()

            @dp.message_handler(state=STG.letters)
            async def ans_let(message:types.message, state: FSMContext):
                letters = message.text
                async with state.proxy() as data:
                    data['letters']=letters

                data = await state.get_data()
                await bot.send_message(message.from_user.id, 'Ты тут1')
                await bot.send_message(message.from_user.id, data['letters'])
                await bot.send_message(message.from_user.id, script.greys(items, data['letters']))
                await state.reset_state()
                await fun1(items)

"""
        elif data['function'] == 'Главное меню':
            await state.reset_state()
            await bot.send_message(message.from_user.id, 'Не то!')
            await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)
            """

@dp.message_handler(Text(startswith='Инфо'),state=None)
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот для помощи в игре "5БУКВ". \nДля старт введите в самой игре любое подходящее слово, а затем начните использовать подсказки бота во вкладке "Новое слово"')

@dp.message_handler(Text(startswith='Главное'),state=None)
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


