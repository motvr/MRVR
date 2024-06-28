import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait



@app.on_message(filters.command(["تفعيل"], ""))
def tom_owners(client: Client, message: Message):
    chat_id = str(message.chat.id)
    Toom = message.from_user
    tom_owners = load_tom_owners()
    tom_admin = load_tom_admin()
    chat_i = message.chat.id
    owner_id = None
    admins = app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
    admins_id = [str(admin.user.id) for admin in admins if not admin.user.is_bot]
    if chat_id not in tom_admin['admin']:
        tom_admin['admin'][chat_id] = {'admin_id': admins_id}
    else:
        existing_admins = tom_admin['admin'][chat_id]['admin_id']
        new_admins = [admin_id for admin_id in admins_id if admin_id not in existing_admins]
        tom_admin['admin'][chat_id]['admin_id'].extend(new_admins)

    dump_tom_admin(tom_admin)
    count = len(new_admins)
    message.reply_text(f"""◍ تم تفعيل الجروب بواسطة [{Toom.first_name}](tg://user?id={Toom.id})\n\n◍ وتمت اضافة {count} مستخدمين الى الادمن
√""")
    
    for member in client.get_chat_members(chat_i, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == enums.ChatMemberStatus.OWNER:
            owner_id = str(member.user.id)
            tooom = member.user
            break
    
    if owner_id is not None:
        if chat_id not in tom_owners['owners']:
            tom_owners['owners'][chat_id] = {'owner_id': [owner_id]}
        else:
            existing_owners = tom_owners['owners'][chat_id]['owner_id']
            if owner_id not in existing_owners:
                tom_owners['owners'][chat_id]['owner_id'].append(owner_id)

        dump_tom_owners(tom_owners)
        message.reply_text(f"""◍ تم تفعيل الجروب بواسطة [{Toom.first_name}](tg://user?id={Toom.id})\n\n◍ وتم رفع [{tooom.first_name}](tg://user?id={tooom.id}) مالك للمجموعة 
√""")
    else:
        message.reply_text("لا يوجد مالك في الدردشة.")