from aiogram import types
from loader import dp, bot 
from keyboards import default, inline



@dp.message_handler(text = "Kurslar")
async def courses(message : types.Message):
    await message.answer(text = "Kurslar ro'yxati", reply_markup=inline.CoursesBtn)


@dp.callback_query_handler(text="arab_lang")
async def arab_lang(call : types.CallbackQuery):
    await call.message.edit_text(text="Arab tili darslari", reply_markup=inline.ArabLangBtn)


@dp.callback_query_handler(text='back_courses')
async def back_courses(call: types.CallbackQuery):
    await call.message.edit_text(text="Kurslar ro'yxati", reply_markup=inline.CoursesBtn)


@dp.callback_query_handler(text="english_lang")
async def english_lang(call: types.CallbackQuery):
    await call.message.edit_text(text="Ingliz tili darslari", reply_markup=inline.EnglishLangBtn)