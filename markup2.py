from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


mainBtn = KeyboardButton('Главное меню')

#Main

startBtn = KeyboardButton('Начать новое слово')
infoBtn = KeyboardButton('Инфо')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(startBtn, infoBtn)

#function
firstBtn = KeyboardButton('Знаю желтую букву')
secondBtn = KeyboardButton('Знаю белую букву')
thirdBtn = KeyboardButton('Знаю серую букву')
forthBtn = KeyboardButton('Знаю серые буквы')
functionMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(firstBtn,secondBtn,thirdBtn, forthBtn, mainBtn)
