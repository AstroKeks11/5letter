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

@dp.message_handler(state=None)
async def bot_message(message: types.Message):
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)

    elif message.text == 'Инфо':
        await bot.send_message(message.from_user.id, 'Бот для помощи в игре "5БУКВ". \nДля старт введите в самой игре любое подходящее слово, а затем начните использовать подсказки бота во вкладке "Новое слово"')

    elif message.text == 'Начать новое слово':
        await bot.send_message(message.from_user.id, 'Новое слово', reply_markup = nav.functionMenu)

        items = script.start()
        #file1 = open('words.txt', 'a')
        #file1.write(items)
        #file1.close()

        await STG.function.set()
        

        @dp.message_handler(state=STG.function)
        async def func_ans(message:types.message, state: FSMContext):
            func = message.text
            async with state.proxy() as data:
                data['func1']=func

                data = await state.get_data()
                func1 = data.get('func1')
                #await bot.send_message(message.from_user.id, 'Ты тут')

                if func1 == 'Знаю желтую букву' or 'Знаю белую букву' or 'Знаю серую букву':
                    await bot.send_message(message.from_user.id, 'Введите букву')
                    await STG.letter.set()

                    @dp.message_handler(state=STG.letter)
                    async def ans_let(message:types.message, state: FSMContext):
                        lett = message.text
                        async with state.proxy() as data:
                            data['lett1']=lett

                        data = await state.get_data()
                        func1 = data.get('func1')
                        if func1 == 'Знаю желтую букву' or 'Знаю белую букву':
                            await bot.send_message(message.from_user.id, 'Введите номер буквы')
                            await STG.place.set()

                            @dp.message_handler(state=STG.place)
                            async def ans_plc(message:types.message, state: FSMContext):
                                plac = message.text
                                async with state.proxy() as data:
                                    data['plac1']=plac

                                data = await state.get_data()
                                func1 = data.get('func1')

                                if func1 == 'Знаю желтую букву':
                                    #file1 = open('words.txt')
                                    #items = file1.read()
                                    #items = script.start()

                                    data = await state.get_data()
                                    letter = data.get('lett1')
                                    place = int(data.get('plac1'))

                                    await bot.send_message(message.from_user.id, script.yellow(items,letter,place))
                                    #file1.close()
                                    await state.finish()
            


                                

                        #data = await state.get_data()
                        #func1 = data.get('func1')
                        #lett1 = message.text
                        #await bot.send_message(message.from_user.id, func1)
                        #await bot.send_message(message.from_user.id, lett1)

                elif func1 == 'Знаю серые буквы':
                   await bot.send_message(message.from_user.id, 'Введите буквы через пробел')
                   await STG.letters.set()

                   @dp.message_handler(state=STG.letters)
                   async def ans_let(message:types.message, state: FSMContext):
                        data = await state.get_data()
                        func1 = data.get('func1')
                        letts1 = message.text
                        await bot.send_message(message.from_user.id, func1)
                        await bot.send_message(message.from_user.id, letts1)

"""        @dp.message_handler(state=STG.letter)
        async def ans_let(message:types.message, state: FSMContext):
            data = await state.get_data()
            func1 = data.get('func1')
            lett1 = message.text
            await bot.send_message(message.from_user.id, func1)
            await bot.send_message(message.from_user.id, lett1)
"""

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


