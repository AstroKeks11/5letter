from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Main

firstBtn = KeyboardButton('Знаю желтую букву')
secondBtn = KeyboardButton('Знаю белую букву')
thirdBtn = KeyboardButton('Знаю серую букву')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(firstBtn,secondBtn,thirdBtn)