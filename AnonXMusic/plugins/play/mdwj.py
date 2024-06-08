import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from asyncio import gather


@app.on_message(
    filters.command(["بايو","البايو"], "")
    & filters.group
    & filters.group
)
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
@app.on_message(
    filters.command(["شخصيتي", "معلوماتي", "شخصيه"], "")
    & filters.group
    & filters.group
)
async def ppdi(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• انـت »   {message.from_user.mention()} يا قلبي ياناس🔥😮‍💨**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
 
 
 
 
@app.on_message(filters.command(["تحويل_لصوره", "تحويل الصوره"], ""))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)], "")
    await m.delete()
    os.remove(f)



@app.on_message(filters.command(["الجروب", "جروب"], "") & filters.group)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🐲 ¦ الاسم » {chat_name}\n🚸 ¦ ايدي الجروب »  -{chat_idd}\n🐊 ¦ رابط » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    