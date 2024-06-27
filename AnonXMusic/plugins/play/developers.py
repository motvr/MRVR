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

#          
                
@app.on_message(
    filters.command(["المبرمج","صياد","مبرمج السورس","زين"], "")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/95648e7a67525895cc50f.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم المبرمج\nللتحدث مع السورس السورس اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᯓ𓆩˹ 𝗠𝗥 𝗩𝗥 ˼𓆪𓆃", url=f"https://t.me/D_Z_J_C"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥", url=f"https://t.me/Jaithon"),
                ],

            ]

        ),

    )
