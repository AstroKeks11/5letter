import config
import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav
import teleScript as script

logging.basicConfig(level=logging.INFO)

bot = Bot(token =config.TOKEN)
dp = Dispatcher(bot)


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
    if message.text == 'Знаю желтую букву':
        await bot.send_message(message.from_user.id, 'Введите букву')


    elif message.text == 'Начать новое слово':
        await bot.send_message(message.from_user.id, 'Новое слово', reply_markup = nav.letterMenu)

        items = script.start()
        await bot.send_message(message.from_user.id, items)
    

    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = nav.mainMenu)


    elif message.text == 'Инфо':
        await bot.send_message(message.from_user.id, 'Бот для помощи в игре "5БУКВ". \nДля старт введите в самой игре любое подходящее слово, а затем начните использовать подсказки бота во вкладке "Новое слово"')

    elif message.text == 'Знаю желтую букву':
        await bot.send_message(message.from_user.id, 'Введите букву')



'''admin'''

'''back'''

#async def yellow():



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)