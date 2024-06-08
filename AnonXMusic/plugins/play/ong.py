import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AnonXMusic import app

@app.on_message(filters.command(['نداء','ن'], ""))
async def call_random_members(client: Client, message: Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_memberss(chat_id)
        if not member.user.is_bot
    ]
    random_members = random.choice(members)
    random_members_mention = f"[{random_members.user.first_name}](tg://user?id={random_members.user.id})"
    random_message = random.choice([
        f"ووين ككارس لنا واجد نرجو فيك 😾 {random_members_mention}",
        f"• يـا قمـري ❤️‍🔥 {random_members_mention}",
        f"حبي فوتك من الخاص وتعال 🤔 {random_members_mention}",
        f"• يـا راس السطل تعال {random_members_mention}",
        f"• انت ليش قمر هكي 🌚♥ {random_members_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')



@app.on_message(filters.command(['زوجني','ز'], ""))
async def call_random_members(client: Client, message: Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_memberss(chat_id)
        if not member.user.is_bot
    ]
    random_members = random.choice(members)
    random_members_mention = f"[{random_members.user.first_name}](tg://user?id={random_members.user.id})"
    random_message = random.choice([
        f"• اخترت لك هذا الشخص {random_members_mention} \n 🙈♥",
        f"• اخترت لك هذا الشخص \n {random_members_mention} \n **"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')