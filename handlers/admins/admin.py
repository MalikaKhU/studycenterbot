from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import default, inline
from loader import dp, db, bot
from data.data import User




def is_admin(user_id):
    user = User(*db.select_user(user_id))
    if user.status == 'admin':
        return True
    return False


@dp.message_handler(text="🧑‍✈️ Admin panel")
async def admin_panel(message: types.Message, state: FSMContext):
    if is_admin(message.from_user.id):
        await message.answer("Admin panel", reply_markup=default.AdminPanel)
    else:
        await message.answer(text=message.text, reply_markup=default.MainMenu(message.from_user.id))
