import asyncio
from keyboards.default.menu_btn import admin, menu
from loader import dp, bot
from aiogram import types

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc

from baza import get_data_tosh, get_data_jizz


jizz_groups = [-1001707553887, -1002120941024, -1002084590316]  # Jizzax guruh ID si

async def send_message(group_id, message):
    try:
        await bot.send_message(chat_id=group_id, text=message)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

async def is_admin(user_id: int) -> bool:
    admins = [1865914991]  # Misol uchun ID lar
    return user_id in admins

scheduler_utc = AsyncIOScheduler(timezone=utc)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Botga xush kelibsiz.")

@dp.message_handler(text='⬅️ oraqa qaytish')
async def admin_command(message: types.Message):
    if await is_admin(message.from_user.id):
        await message.answer("Bosh menudasiz", reply_markup=menu)
    else:
        await message.answer("Uzr, siz admin emassiz.")
@dp.message_handler(text='admin')
async def admin_command(message: types.Message):
    if await is_admin(message.from_user.id):
        await message.answer("Admin paneliga xush kelibsiz!", reply_markup=admin)
    else:
        await message.answer("Uzr, siz admin emassiz.")

@dp.message_handler(text='Toshkentni yoqish')
async def tosh_command(message: types.Message):
    if await is_admin(message.from_user.id):
        global tosh_scheduler
        await message.answer("Toshkent xabarlarni har 5 sekundda yuboraman.")
        tosh_scheduler = AsyncIOScheduler(timezone=utc)
        tosh_scheduler.start()
        asyncio.create_task(send_tosh_message())
        tosh_scheduler.add_job(send_tosh_message, "interval", seconds=5)
    else:
        await message.answer("Uzr, siz admin emassiz.")

# Stop Tosh komandasi
@dp.message_handler(text="Toshkentni o'chirish")
async def stoptosh_command(message: types.Message):
    if await is_admin(message.from_user.id):
        global tosh_scheduler
        await message.answer("Toshkent xabarlarni to'xtataman.")
        tosh_scheduler.shutdown()
    else:
        await message.answer("Uzr, siz admin emassiz.")

# Jizz komandasi
@dp.message_handler(text='Jizzaxni yoqish')
async def jizz_command(message: types.Message):
    if await is_admin(message.from_user.id):
        global jizz_scheduler
        await message.answer("Jizzax xabarlarni har 5 sekundda yuboraman.")
        jizz_scheduler = AsyncIOScheduler(timezone=utc)
        jizz_scheduler.start()
        asyncio.create_task(send_jizz_message())
        jizz_scheduler.add_job(send_jizz_message, "interval", seconds=5)
    else:
        await message.answer("Uzr, siz admin emassiz.")

# Stop Jizz komandasi
@dp.message_handler(text="Jizzaxni o'chirish")
async def stopjizz_command(message: types.Message):
    if await is_admin(message.from_user.id):
        global jizz_scheduler
        await message.answer("Jizzax xabarlarni to'xtataman.")
        jizz_scheduler.shutdown()
    else:
        await message.answer("Uzr, siz admin emassiz.")

async def send_tosh_message():
    message = "TOSHKENTDAN\n\nJIZZAXGA\n\nODAM POCHTA\n\nTOM BAGAJ BOR\n\nPOCHTA OLAMIZ\n\nTOM BAGAJ BOR\n\n904979494\n\nTOSHKENTDAN\n\nJIZZAXGA\n\nPOCHTA\n\nOdam OLAMIZ\n\nTOM BAGAJ BOR\n\nPOCHTA OLAMIZ\n\nTOM BAGAJ BOR\n\n904979494"
    for group_id in jizz_groups:
        await send_message(group_id, message)

async def send_jizz_message():
    message = "⏭.JIZZAXDAN\n\n⏯.TOSHKENT\n\n🙍. ODAM \n\n🧳. POCHTA OLAMIZ \n\nTom baGaj bor\n\n904979494\n\n.⏭.JIZZAXDAN\n\n⏯.TOSHKENTGA \n\n🙍. ODAM \n\n🧳. POCHTA OLAMIZ \n\nTom baGaj bor\n\n904979494!"
    for group_id in jizz_groups:
        await send_message(group_id, message)

# Asosiy funksiya
async def main():
    global tosh_scheduler, jizz_scheduler
    print("Bot ishga tushdi.")
    await bot.delete_webhook()

    await dp.start_polling()

    # Schedulerlarni ishga tushirish
    scheduler_utc.start()
    tosh_scheduler = AsyncIOScheduler(timezone=utc)
    jizz_scheduler = AsyncIOScheduler(timezone=utc)
    tosh_scheduler.start()
    jizz_scheduler.start()
    asyncio.create_task(send_tosh_message())
    asyncio.create_task(send_jizz_message())

# Dasturni boshlash
if __name__ == "__main__":
    asyncio.run(main())
