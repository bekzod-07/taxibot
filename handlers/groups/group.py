from aiogram import types
from loader import dp, bot
import logging

logging.basicConfig(level=logging.INFO)

allowed_group_chat_ids = [-1001170798978, -1001797195073, -1001799096541]  # List of allowed group chat IDs
forward_chat_id = -1002009198668  # Destination chat ID for forwarding messages
disallowed_user_ids = [5816736795, 862452906, 1349806769, 35080150, 1753033938, 406795002]  # List of disallowed user IDs for forwarding messages

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo_message(msg: types.Message):
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    user = await bot.get_chat_member(chat_id, user_id)
    message_text = msg.text

    if chat_id in allowed_group_chat_ids:
        if user_id not in disallowed_user_ids:
            if not msg.forward_from_chat:
                try:
                    # Forward the message
                    forward_msg = await bot.forward_message(chat_id=forward_chat_id, from_chat_id=chat_id, message_id=msg.message_id)

                    # Extract user's first name and last name
                    user_first_name = msg.from_user.first_name
                    user_last_name = msg.from_user.last_name

                    forward_text = f"ASSALOMU ALEYKUM\n\nSIZNING ZAKAZINGIZ LIDER\n\nSHAFYORLAR GURUHIGA TUSHDI✅\n\nLICHKADA ISHONCHLI SHAFYORLARIMIZ KUTMOQDA❗️"
                    await bot.send_message(chat_id, forward_text, parse_mode="markdown")
                except Exception as e:
                    logging.error(f"Error occurred: {e}")
                finally:
                    await bot.delete_message(chat_id=chat_id, message_id=msg.message_id)
            else:
                pass
        else:
            pass
