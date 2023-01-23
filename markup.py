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

#letters
aBtn = InlineKeyboardButton(text = 'А', callback_data= 'letter_А')
bBtn = InlineKeyboardButton(text = 'Б', callback_data= 'letter_Б')
vBtn = InlineKeyboardButton(text = 'В', callback_data= 'letter_В')
gBtn = InlineKeyboardButton(text = 'Г', callback_data= 'letter_Г')
dBtn = InlineKeyboardButton(text = 'Д', callback_data= 'letter_Д')
lettersMenu = InlineKeyboardMarkup(row_width=5).add(aBtn, bBtn, vBtn, gBtn, dBtn)

#places
firstPl = InlineKeyboardButton(text = '1', callback_data= 'pl_1')
secondPl = InlineKeyboardButton(text = '2', callback_data= 'pl_2')
thirdPl = InlineKeyboardButton(text = '3', callback_data= 'pl_3')
forthPl = InlineKeyboardButton(text = '4', callback_data= 'pl_4')
fifthPl = InlineKeyboardButton(text = '5', callback_data= 'pl_5')
placeMenu = InlineKeyboardMarkup(row_width=1).add(firstPl, secondPl, thirdPl, forthPl, fifthPl)

#cycle
cBtn = InlineKeyboardButton(text='Просеять',callback_data='cycle')
cMenu = InlineKeyboardMarkup(row_width=1).add(cBtn)