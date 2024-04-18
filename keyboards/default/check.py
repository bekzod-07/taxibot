from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

check_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ha"),
            KeyboardButton("Yo'q"),
        ],

    ], resize_keyboard=True
)