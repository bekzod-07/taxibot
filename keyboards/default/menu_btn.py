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
            KeyboardButton(text="Jizzax Toshkent"),
            KeyboardButton(text="Toshkent Jizzax"),
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

admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkentni yoqish"),
            KeyboardButton(text="Toshkentni o'chirish"),
        ],
        [
            KeyboardButton(text="Jizzaxni yoqish"),
            KeyboardButton(text="Jizzaxni o'chirish"),
        ],

        [
            KeyboardButton(text="⬅️ oraqa qaytish")
        ],
    ], resize_keyboard=True
)
