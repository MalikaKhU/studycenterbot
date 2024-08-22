from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.data import User
from loader import db


MenuBtn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MenuBtn.insert(KeyboardButton(text="O'quv kurslar"))
MenuBtn.insert(KeyboardButton(text="Kurslar"))
MenuBtn.insert(KeyboardButton(text="Fayllar"))
MenuBtn.insert(KeyboardButton(text="O'qtuvchilar haqida ma'lumot"))
MenuBtn.insert(KeyboardButton(text="Natijalar"))
MenuBtn.insert(KeyboardButton("Ro'yxatdan o'tish"))

FilesBtn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
FilesBtn.insert(KeyboardButton(text="Rasm"))
FilesBtn.insert(KeyboardButton(text="Rasm1"))
FilesBtn.insert(KeyboardButton(text="Rasm2"))
FilesBtn.insert(KeyboardButton(text='Orqaga'))

GroupBtn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
group_list = ["Arab tili noldan", "Arab tili grammatikasi", "Cefr/AtTanal", "Orqaga"]
for group in group_list:
    GroupBtn.insert(KeyboardButton(text=group))


ArabiczeroBtn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
Arabiczero_list = ["Ro'yxatdan o'tish", "Orqaga"]
for arabiczero in Arabiczero_list:
    ArabiczeroBtn.insert(KeyboardButton(text=arabiczero))

GrammaBtn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
gramma_list = ["Ro'yxatdan o'tish", "Orqaga"]
for gramma in gramma_list: 
    GrammaBtn.insert(KeyboardButton(text=gramma))

CefrBtn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
cefr_list = ["Ro'yxatdan o'tish", "Orqaga"]
for cefr in cefr_list: 
    CefrBtn.insert(KeyboardButton(text=cefr))

InfoBtn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
info_list = ["Ro'yxatdan o'tish", "Orqaga"]
for info in info_list:
    InfoBtn.insert(KeyboardButton(text=info))


ResultBtn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
result_list = ["Ro'yxatdan o'tish", "Orqaga"]
for result in result_list:
    ResultBtn.insert(KeyboardButton(text=result))





