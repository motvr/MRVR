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

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_video(
                            video = f"https://telegra.ph/file/a3053a30b341b3a8bc85e.mp4",
                            caption = f"⎉ اهلا انا بوت تصفيه مجموعات , استطيع حظر 1000 شخص خلال دقيقه 🕜\n\nللحصول علي كود حظر الاعضاء تواصل مع المطور 🔎\n\n↞ انضـم هنا @AlmortagelTech",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المـطور", url=f"https://t.me/{OWNER}")
                ]       
           ]
      )
)

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
