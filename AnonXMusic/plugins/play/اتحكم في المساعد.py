from pyrogram import filters, Client
from AnonXMusic import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError
#HHC3C4
@app.on_message(filters.regex("اسم المساعد"))
async def tom_name(client, message):
    assistant = await group_assistant(Anony, message.chat.id)
    await message.reply("ارسل اسم المساعد الجديد:")
    try:
        new_name = await client.ask(message.chat.id, "اكتب اسم المساعد الجديد:")
        await assistant.update_profile(first_name=new_name)
        await message.reply(f"تم تغيير اسم المساعد الى {new_name}")
    except Exception as e:
        await message.reply("حدث خطأ اثناء تغيير اسم المساعد!")
