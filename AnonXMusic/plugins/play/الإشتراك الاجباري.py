from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app
from config import Jaithon 

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not Jaithon:
        return
    try:
        try:
            await app.get_chat_member(Jaithon, msg.from_user.id)
        except UserNotParticipant:
            if Muntazer.isalpha():
                link = "https://t.me/Jaithon"
            else:
                chat_info = await app.get_chat(Jaithon)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙عزيزي {msg.from_user.mention} \n~︙عليك الأشتراك في قناة البوت \n~︙قناة البوت : @Jaithon",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(" ❝ 𝗦𝗼𝘂𝗿𝗰𝗲➠𝗩𝗥 ❞ ", url=https://t.me/Jaithon)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {Jaithon}!")
