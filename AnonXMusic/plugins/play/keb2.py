import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(filters.command(["اصدار"], ""))
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""**⋖━━❲𖣂❳━━●○ᴀʟᴍᴏʀᴛᴀɢᴇʟ○●━━❲𖣂❳━━⋗**\nمرحبا بك عزيزي {message.from_user.mention}\n
♡♕᚜ اسم سورس:-المرتجل
♡♕᚜ نوعه:-ميوزك
♡♕᚜ للغه برمجه:- بايثون
♡♕᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
♡♕᚜ مجال تشغيل :- تشغيل بوتات الميوزك
♡♕᚜ نظام تشغيل:-المرتجل بوت ميوزك
♡♕᚜ الاصدار 4.0.1 pyrogram 
♡♕᚜ تاريخ تاسيس:-10-4-2020

**⋖━━❲𖣂❳━━●○ᴀʟᴍᴏʀᴛᴀɢᴇʟ○●━━❲𖣂❳━━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "●━◉⟞⟦ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⟧⟝◉━●", url=f"https://t.me/AlmortagelTech"), 
               ],
          ]
        ),
    )


