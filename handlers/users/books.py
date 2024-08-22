from aiogram import types
from loader import dp, bot 
from keyboards import default, inline




@dp.message_handler(text="O'quv kurslar") 
async def group(message: types.Message):
    await message.answer(text="Kurslardan birini tanlang", reply_markup=default.GroupBtn)


@dp.message_handler(text="Ro'yxatdan o'tish")
async def regis(message:types.Message):
    await message.answer(text="Ro'yxatdan o'tish uchun Ism, Familya va Telefon raqamingizni qoldiring siz bilan tez oraqa bog'lanamiz.")

@dp.message_handler(text="Arab tili noldan")
async def arab_lang(message:types.Message):
    await message.answer(text="Bu kurs arab tilini umuman bilmaydigan o'quvchilar uchun moljallangan. Kurs davomida 'Boshlang'ich arab tili saboqlari' kitobi otiladi. Dars kunlari: Dushanba, Chorshanba, Juma, soat 14:00da. Ro'yxatdan o'tish uchun ro'yxatdan o'tish tugmasini bosing.",reply_markup=default.ArabiczeroBtn)


@dp.message_handler(text="Arab tili grammatikasi") 
async def gramma(message: types.Message):
    await message.answer(text="Bu kurs arab tilini boshlang'ich darajada biladigan o'quvchilar uchun mo'ljallangan. Kurs davomida grammatikaga oid maxsus kitoblar o'tiladi. Dars kunlari: Seshanba, Payshanba, Shanba kunlari, soat 14:00da. Ro'yxatdan o'tish uchun ro'yxatdan o'tish tugmasini bosing.", reply_markup=default.GrammaBtn)


@dp.message_handler(text="Cefr/AtTanal")
async def cefr(message:types.Message):
    await message.answer(text="Bu kurs sodda matnlarni tarjima qila oladigan, sarf va nahvlarni tugatgan o'quvchilar uchun mo'ljallangan. Kurs davomida Cefr va At Tanal testiga tayyorlash uchun maxsus kitoblar o'tiladi. Dars kunlari: Dushanba, Chorshanba, Juma, soat 16:00da. Ro'yxatdan o'tish uchun ro'yxatdan o'tish tugmasini bosing.", reply_markup=default.CefrBtn)


@dp.message_handler(text="Orqaga")
async def group(message: types.Message): 
    await message.answer(text="Asosiy menyu", reply_markup=default.MenuBtn)


@dp.message_handler(text="O'qtuvchilar haqida ma'lumot")
async def teacher(message: types.Message):
    await message.answer(text="Ustoza Malika: Cefrdan C1 sohibasi, ko'p yillik dars berish tarjibasi, mingdan ortiq o'quvchilar ustozasi.", reply_markup=default.InfoBtn)


@dp.message_handler(text="Natijalar")
async def result(message: types.Message):
    await message.answer(text="Xolnazarova Malika 9 oyda C1 sohibasiga aylandi.", reply_markup=default.ResultBtn)