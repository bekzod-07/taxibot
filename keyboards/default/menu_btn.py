from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🚖 Taxi bo'lish"),
            KeyboardButton(text="🤵 Yo'lovchi bo'lish"),
        ],
    ],
    resize_keyboard=True
)

yonalish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Farg'onadan Gorskiy"),
            KeyboardButton(text="Gorskiydan Farg'ona"),
        ],
        [
            KeyboardButton(text="⬅️ Bekor qilish")
        ]
    ], resize_keyboard=True
)

yolovchii = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📦 Pochta bor"),
        ],
        [
            KeyboardButton(text="1 kishi"),
            KeyboardButton(text="2 kishi"),
        ],
        [
            KeyboardButton(text="3 kishi"),
            KeyboardButton(text="4 kishi"),
        ],
        [
            KeyboardButton(text="⬅️ Bekor qilish")
        ],
    ], resize_keyboard=True
)