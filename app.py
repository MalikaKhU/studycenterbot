from aiogram import executor
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.admins.functions import scheduler
import asyncio


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    asyncio.create_task(scheduler())
    

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

# Botni ishga tushirish uchun faqat app.py ga run bering tushunarli xop
