from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


CoursesBtn = InlineKeyboardMarkup(row_width = 2)
CoursesBtn.insert(InlineKeyboardButton(text="Arab tili", callback_data='arab_lang'))
CoursesBtn.insert(InlineKeyboardButton(text="Ingliz tili", callback_data='english_lang'))
CoursesBtn.insert(InlineKeyboardButton(text="Rus tili", url='https://www.youtube.com/watch?v=ciKhbKxJcns'))


ArabLangBtn = InlineKeyboardMarkup(row_width = 2)
ArabLangBtn.insert(InlineKeyboardButton(text='1-dars', url='https://youtu.be/KIxaisq3hQk?si=LJAB3Z6VctzNYlLV'))
ArabLangBtn.insert(InlineKeyboardButton(text='2-dars', url='https://youtu.be/VwBt5XyaYhM?si=uHkIw9jf9In5Fkau'))
ArabLangBtn.insert(InlineKeyboardButton(text='3-dars', url='https://youtu.be/dPrvk9QLRys?si=5GptP1va6oOsuAJP'))
ArabLangBtn.insert(InlineKeyboardButton(text='4-dars', url='https://youtu.be/1eSa7xaxUOY?si=XaHwYapWFKrGFo3l'))
ArabLangBtn.insert(InlineKeyboardButton(text='5-dars', url='https://youtu.be/3bJZcW9Bxxw?si=stDD7Fex1f1TLfmG'))
ArabLangBtn.insert(InlineKeyboardButton(text='6-dars', url='https://youtu.be/vxpn8EujZiw?si=g_g0bxSxFlhIMn3k'))
ArabLangBtn.insert(InlineKeyboardButton(text="Orqaga", callback_data='back_courses'))


EnglishLangBtn = InlineKeyboardMarkup(row_width = 2)
EnglishLangBtn.insert(InlineKeyboardButton(text="1-dars", url="https://youtu.be/n-uTwzzVnsg?si=wArY1L7dBdgYpa-m"))
EnglishLangBtn.insert(InlineKeyboardButton(text="2-dars", url="https://youtu.be/0Gi1DknYo5A?si=y3Kba0AFwgA7vyvV"))
EnglishLangBtn.insert(InlineKeyboardButton(text="3-dars", url="https://youtu.be/MsrT1z4EuOg?si=r0nS8i5cCYBl7KNl"))
EnglishLangBtn.insert(InlineKeyboardButton(text="4-dars", url="https://youtu.be/erJ1qmuZW6Q?si=7IGbn9sahAlAFWGz"))
EnglishLangBtn.insert(InlineKeyboardButton(text="5-dars", url="https://youtu.be/IL_008MAgwQ?si=ph8Dd2EA-DANiwgO"))
EnglishLangBtn.insert(InlineKeyboardButton(text="6-dars", url="https://youtu.be/EmWHDcJKLbE?si=oj2BzQAOsDH3dN0T"))
EnglishLangBtn.insert(InlineKeyboardButton(text="Orqaga", callback_data='back_courses'))
# Vazifa YouTubedan biror kursni botga kiritish inline btn bn
# Ingliz tilida url qoshish va orqaga qaytarish
# Rasm tagida caption and button

