from aiogram import types
from loader import dp, bot
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

allowed_group_chat_ids = [-1001799096541, -1001170798978, -1001797195073]
forward_chat_id = -1002009198668
disallowed_user_ids = [2053644093, 1538317970, 406795002, 321309026, 6653637615, 5284392977, 6660029795, 1753033938, 6366509243, 862452906, 517370314, 1319597388, 5280935053, 1349806769, 35080150, 106617532, 6375301950, 6560156377, 654372379]

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo_message(msg: types.Message):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    user = await bot.get_chat_member(chat_id, user_id)
    message_text = msg.text

    if chat_id in allowed_group_chat_ids and user_id not in disallowed_user_ids and not msg.forward_from_chat:
        try:
            # Forward the message
            forward_msg = await bot.forward_message(chat_id=forward_chat_id, from_chat_id=chat_id, message_id=msg.message_id)
            user_first_name = msg.from_user.first_name

            # Construct the forward message
            forward_text = f"ASSALOMU ALEYKUM #{user_first_name}\n\nSIZNING ZAKAZINGIZ LIDER\n\nSHAFYORLAR GURUHIGA TUSHDI✅\n\nLICHKADA ISHONCHLI SHAFYORLARIMIZ KUTMOQDA❗️)\n\nTezkor taksi xizmati 🕓24/7\n\nhttps://t.me/Fargona_Goriskiy_roBot"
            # Send the custom message
            sent_message = await bot.send_message(chat_id, forward_text)
            await asyncio.sleep(0.005)
            # Delete the sent message
            await bot.delete_message(chat_id=chat_id, message_id=msg.message_id)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
        finally:
            await asyncio.sleep(7)
            await bot.delete_message(chat_id=chat_id, message_id=sent_message.message_id)
