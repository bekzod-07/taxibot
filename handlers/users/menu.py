from aiogram import types

from keyboards.default.check import check_btn
from keyboards.default.menu_btn import yonalish, yolovchii, menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from states.data import kursgaYozilish

@dp.message_handler(text="🤵 Yo'lovchi bo'lish")
async def kursga_yozilish(message: types.message, state: FSMContext):
    await message.answer("🚖 Taksi chaqirish uchun ariza berish.\n\n"
                         "Hozir sizga bir necha savollar beriladi, har biriga javob bering va arizangiz operatorga yuboriladi.")
    await message.answer("Bormoqchi bo'lgan yo'nalishingizni belgilang📍.", reply_markup=yonalish)
    await kursgaYozilish.yolovchi.set()

@dp.message_handler(state=kursgaYozilish.yolovchi)
async def yolovchi(message: types.Message, state: FSMContext):
    yolovchi = message.text
    await state.update_data({"Qayerga boradi": yolovchi})
    await message.answer("👥 Nechta yo'lovchi bor yoki 📦 pochta.", reply_markup=yolovchii)
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.odam)
async def odam(message: types.Message, state: FSMContext):
    odam = message.text
    await state.update_data({"Odam yoki pochta bor": odam})
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Telefon raqamingizni +998 bilan kiriting\n\nmasalan: +998901235678", reply_markup=remove_keyboard)
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.teleraqam)
async def teleraqam(message: types.Message, state: FSMContext):
    teleraqam = message.text
    await state.update_data({"Nomer": teleraqam})

    data = await state.get_data()
    yolovchi = data.get("Qayerga boradi")
    odam = data.get("Odam yoki pochta bor")
    teleraqam = data.get("Nomer")

    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f" Yo'lovchi: {yolovchi}\n"
    msg += f" Odam yoki pochta bor: {odam}\n"
    msg += f" Aloqa: {teleraqam}"
    await message.answer(msg)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=check_btn)
    await kursgaYozilish.next()


@dp.message_handler(state=kursgaYozilish.check)
async def check(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
        yolovchi = data.get("Qayerga boradi")
        odam = data.get("Odam yoki pochta bor")
        teleraqam = data.get("Nomer")

        msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
        msg += f" Yo'lovchi: {yolovchi}\n"
        msg += f" Odam yoki pochta bor: {odam}\n"
        msg += f" Aloqa: {teleraqam}"
        await message.answer(msg)
        await bot.send_message(chat_id=1865914991, text=msg)
        await message.answer("Barcha ma`lumotlar adminga yuborildi. Tez orada siz bilan bog`lanadi")
        await message.answer("Bosh menyu!", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Qabul qilinmadi", reply_markup=menu)
        await state.finish()
