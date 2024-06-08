import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from AnonXMusic.plugins.play.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from AnonXMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cec7b12365a2dad6d9b8e.jpg",
        caption=f"""<b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» استخـدم الازرار بالاسفـل\n» لـ تصفـح اوامـر بـوت فير</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〔 اوامــر التشغيــل 〕", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "〔 اوامـر القنـاة 〕", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "〔 اوامـر الادمـن 〕", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "〔 اوامــر المطــور 〕", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "〔 مبـرمج السـورس 〕", url="https://t.me/D_Z_J_C"),
                ],
            ]
        ),
    )
