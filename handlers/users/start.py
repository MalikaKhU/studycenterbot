from aiogram import types
from loader import dp, bot 
from keyboards import default, inline


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="Assalomu alaykum!  Xush kelibsiz😊", 
                    reply_markup=default.MenuBtn)

# Hello world