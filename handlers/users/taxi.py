from aiogram import types

from keyboards.default.check import check_btn
from keyboards.default.menu_btn import menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from states.data import taxi

@dp.message_handler(text="🚖 Taxi bo'lish")
async def bot_start(message: types.Message):
    await message.answer(f"🚖 Taksi bo'lish uchun ariza yuborish.\n\n"
                         "Hozir sizga bir necha savollar beriladi, har biriga javob bering va arizangiz operatorga yuboriladi.")

    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("👥 Ismingizni kiriting", reply_markup=remove_keyboard)
    await taxi.fio.set()

@dp.message_handler(state=taxi.fio)
async def yolovchi(message: types.Message, state: FSMContext):
    fio = message.text
    await state.update_data({"Ism": fio})
    await message.answer("Telefon raqamingizni +998 bilan kiriting\n\nmasalan: +998901235678")
    await taxi.next()

@dp.message_handler(state=taxi.teleraqam)
async def teleraqam(message: types.Message, state: FSMContext):
    teleraqam = message.text
    await state.update_data({"Telefon raqam": teleraqam})

    data = await state.get_data()
    fio = data.get("Ism")
    teleraqam = data.get("Telefon raqam")

    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f" Taksichi: {fio}\n"
    msg += f" Telefon raqam: {teleraqam}"
    await message.answer(msg)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=check_btn)
    await taxi.next()


@dp.message_handler(state=taxi.check)
async def check(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":

        data = await state.get_data()
        fio = data.get("Ism")
        teleraqam = data.get("Telefon raqam")

        msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
        msg += f" Taksichi: {fio}\n"
        msg += f" Telefon raqam: {teleraqam}"
        await message.answer(msg)
        await bot.send_message(chat_id=1865914991, text=msg)
        await message.answer("Barcha ma`lumotlar adminga yuborildi. Tez orada siz bilan bog`lanadi")
        await message.answer("Bosh menyu!", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Qabul qilinmadi", reply_markup=menu)
        await state.finish()
