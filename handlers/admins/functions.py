from loader import *
from aiogram.types import Message, InputFile, ContentType
from aiogram.dispatcher import FSMContext
from states.States import States
from data.config import ADMINS
import aioschedule
import asyncio


@dp.message_handler(commands=['download'], user_id=ADMINS)
async def download_handler(message: Message):
    try:
        await message.answer_document(
            document = InputFile(path_or_bytesio='data/main.db'),
        )
    except:
        await message.answer('Something went wrong with download database.')


@dp.message_handler(commands=['upload'], user_id=ADMINS)
async def download_handler(message: Message):
    await message.answer(text="Send main.db file:")
    await States.UploadDB.set()


@dp.message_handler(state=States.UploadDB, content_types=types.ContentTypes.DOCUMENT)
async def upload_db(message: types.Message, state: FSMContext):
    await message.document.download(destination_file='data/main.db')
    await state.reset_state()
    
    await message.reply(text="✅ File uploaded!")


async def download():
    try:
        await bot.send_document(
            chat_id = ADMINS[0],
            document = InputFile(path_or_bytesio='data/main.db')
        )
    except:
        pass


async def scheduler():
    aioschedule.every().day.at('00:00').do(download)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)