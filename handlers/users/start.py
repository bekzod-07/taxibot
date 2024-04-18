from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.menu_btn import menu
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n\nHaydovchimisiz yoki Yulovchi?", reply_markup=menu)

@dp.message_handler(text='⬅️ Bekor qilish')
async def bot_start(message: types.Message):
    await message.answer(f"Bosh menuga qaytdingiz. Kerakli bo'limni tanlang", reply_markup=menu)
