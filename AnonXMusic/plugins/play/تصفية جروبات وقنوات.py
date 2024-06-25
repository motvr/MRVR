import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired
from AnonXMusic import app

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(filters.command(["انطر ابلاكاش"], ""))
async def banall_command(client, message: Message):
    print("الحصول على أعضاء من {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("طردته {} من {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("لم استطيع حظر : {} \n مـن : {}".format(i.user.id, e))           
    print("process completed")
