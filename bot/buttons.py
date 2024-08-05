from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data_base import Menyu_Sql, Food_Sql, Taomlar, Ichimliklar



phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="telefon nomr ulashish", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


menyu = InlineKeyboardBuilder()

for tugnma in Menyu_Sql():
    menyu.button(text=f"{tugnma[1]}", callback_data=f"{tugnma[1]}")
menyu.add(InlineKeyboardButton(text=f"Zakaz berish 🧺", callback_data='zakaz'))
menyu.adjust(2)


taomlar = InlineKeyboardBuilder()

for tugnma in Taomlar():
    taomlar.button(text=f"{tugnma[1]}", callback_data=f"{tugnma[1]}")
taomlar.add(InlineKeyboardButton(text=f"maxsulot qoshish", callback_data='qoshish'))
taomlar.adjust(2)

ichimliklar = InlineKeyboardBuilder()

for tugnma in Ichimliklar():
    ichimliklar.button(text=f"{tugnma[1]}", callback_data=f"{tugnma[1]}")
ichimliklar.add(InlineKeyboardButton(text=f"maxsulot qoshish", callback_data='qoshish'))
ichimliklar.adjust(2)