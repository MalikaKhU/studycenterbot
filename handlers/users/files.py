from aiogram import types
from loader import dp, bot 
from keyboards import default, inline


@dp.message_handler(text="Fayllar")
async def files(message: types.Message):
    await message.answer(text="Fayllar", reply_markup=default.FilesBtn)


@dp.message_handler(text='Rasm')
async def picture(message: types.Message):
    await message.answer_photo(
        photo = types.InputFile(path_or_bytesio='data/big-love.jpg'),
        caption="Shunchaki rasm")
    await message.answer_photo(
        photo = "https://storage.kun.uz/source/10/ZQctk0fnx-jq2yQMqDzYkBKZvN98LeeJ.jpg",
        caption="Talabalar", 
        reply_markup=inline.ArabLangBtn
    )

@dp.message_handler(text = 'Image')
async def image(message: types.Message):
    await message.answer_photo(
        photo= types.InputFile(path_or_bytesio="data/web programmer.jpg"),
        caption="I am a programmer ")
    await message.answer_photo(
        photo="https://c7.alamy.com/comp/T00PNM/portrait-of-young-muslim-african-american-female-software-developer-with-blue-scarf-standing-at-modern-startup-office-T00PNM.jpg",
        reply_markup = inline.EnglishLangBtn
    )
