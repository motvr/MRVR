
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

@app.on_message(
    filters.command(["سورس مين","سورس","السورس","سورسي", "𝗠𝗥 𝗩𝗥"], ""))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e1afd8ed6c94fe4b3a270.jpg",
        caption=f"""Welcome to ѕᴏụʀᴄᴇ vr""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                text="𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥", url=f"https://t.me/Jaithon"
                        ),
           InlineKeyboardButton(
                text="𝗚𝗿𝗼𝘂𝗽", url=f"https://t.me/Source_MRVR"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗠𝗥 𝗩𝗥", url=f"https://t.me/D_Z_J_C"
            ),
  
                ],

            ]

        ),

    )


@app.on_message(filters.command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )