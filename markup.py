from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainBtn = KeyboardButton('Главное меню')

#Main

startBtn = KeyboardButton('Начать новое слово')
infoBtn = KeyboardButton('Инфо')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(startBtn, infoBtn)

#letters
firstBtn = KeyboardButton('Знаю желтую букву')
secondBtn = KeyboardButton('Знаю белую букву')
thirdBtn = KeyboardButton('Знаю серую букву')
forthBtn = KeyboardButton('Знаю серые буквы')
letterMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(firstBtn,secondBtn,thirdBtn, forthBtn, mainBtn)