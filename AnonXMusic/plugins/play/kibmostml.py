import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AnonXMusic import app
from random import  choice, randint

@app.on_message(filters.command(["صوره", "🕷", "صورهه", "صور"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار صوره لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["انميي", "انمي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,153)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار انمي لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["متحركه. 🎬", "متحركه"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,926)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="💙 ¦ تـم اختيـار ملصق لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["تلاوات", "تلاوة"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(24,618)
    url = f"https://t.me/EIEI06/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار تلاوة قرآنيه لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["اقتباسات", "اقتباس"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,102)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار اقتباس لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["هيدرا", "هيدرات"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,153)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار هيدرات لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["صور", "افاتار بنات"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,216)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار افاتار بنات لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["صور شباب", "افاتار شباب"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار افاتار شباب لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["سوره", "قران"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,82)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار ايـه قرآنيه لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["الشيخ", "النقشبندي", "نقشبندي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,114)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["عبدالباسط", "عبدالباسط عبدالصمد"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(7,265)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["استوري", "استوريهات. 🥹"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="💚 ¦ تـم اختيـار استوري لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

