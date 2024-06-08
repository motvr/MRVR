import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from AnonXMusic.plugins.play.filters import command
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
from datetime import datetime

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from AnonXMusic.plugins.play.filters import command
from AnonXMusic import app


ksdof = []
@app.on_message(command(["قفل كشف", "تعطيل كشف"]), group=2272)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in ksdof:
        return await message.reply_text("تم معطل من قبل🔒")
      ksdof.append(message.chat.id)
      return await message.reply_text("تم تعطيل كشف بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(command(["فتح كشف", "تفعيل كشف"]), group=2292)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in ksdof:
        return await message.reply_text("كشف مفعل من قبل ✅")
      ksdof.remove(message.chat.id)
      return await message.reply_text("تم فتح كشف بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(command(["كشف"]), group=27722)
async def iddd(client, message):
    if message.chat.id in ksdof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""
┏━━━━━━━━━━━━━━⧫
┠**<b>معـلومات الشخـص 🖤🤸‍♂️</b>**
┗━━━━━━━━━━━━━━⧫
 ⦿ الاسم ‣ : {message.from_user.mention}\n⦿ يـوزرك ☀️ ‣: @{message.from_user.username}\n⦿ الايـدي 💎 ‣: {message.from_user.id}\n⦿ جروب ‣ : {message.chat.title}\n⦿ ايدي الجروب ☀️ ‣ : {message.chat.id}\n⦿ البـايو ‣: {usr.bio}""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    

