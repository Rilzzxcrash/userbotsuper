import aiohttp
import filetype
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ϙᴜᴏᴛᴇs ᴠɪᴅᴇᴏ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ϙᴜᴏᴛᴇs ᴠɪᴅᴇᴏ ⦫</b>
<blockquote>
⎆ perintah :
ᚗ <code>{0}qvideo</code> Link

⎆ ᴘᴇɴᴊᴇʟᴀsᴀɴ:
⊶ Membuat Quotes video seperti tiktok.
</blockquote>
"""


async def upload_media(m: Message):
    media = await m.reply_to_message.download()
    try:
        with open(media, "rb") as file:
            file_data = file.read()
            ext = filetype.guess_extension(file_data) or "unknown"
        
        form_data = aiohttp.FormData()
        form_data.add_field("fileToUpload", open(media, "rb"), filename=f"file.{ext}")
        form_data.add_field("reqtype", "fileupload")
        
        async with aiohttp.ClientSession() as session:
            async with session.post("https://catbox.moe/user/api.php", data=form_data) as res:
                if res.status == 200:
                    url = await res.text()
                    return url.strip()
                else:
                    return None
    finally:
        os.remove(media)

@PY.UBOT("qvideo")
async def quotesvideo_handler(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.video:
        return await message.reply("Silakan balas ke sebuah video dengan perintah: `/qvideo teks`")

    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("Silakan masukkan teks untuk quotes video.\nContoh: `/qvideo Makan Ayam`")

    msg = await message.reply("🔄 Mengunggah video...")
    video_url = await upload_media(message)

    if not video_url:
        return await msg.edit("❌ Gagal mengunggah video!")

    await msg.edit("🎥 Membuat Quotes Video...")
    
    api_url = f"https://api.botcahx.eu.org/api/maker/quotesvideo?url={video_url}&text={query}&apikey=moire"
    res = requests.get(api_url)

    if res.status_code == 200:
        data = res.json()
        if "result" in data:
            video_result_url = data["result"]
            return await message.reply_video(video_result_url, caption="✅ Quotes Video berhasil dibuat!")
        return await msg.edit("❌ Gagal membuat quotes video.")
    
    return await msg.edit(f"❌ Gagal mendapatkan hasil (Status: {res.status_code})")
            
