import config
import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token =config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)