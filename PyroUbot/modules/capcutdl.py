from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴄᴀᴘᴄᴜᴛ ᴅʟ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴀᴘᴄᴜᴛ ᴅʟ ⦫</b>
<blockquote>
⎆ perintah :
ᚗ <code>{0}capdl</code> Link

⎆ ᴘᴇɴᴊᴇʟᴀsᴀɴ:
⊶ Download template capcut.
</blockquote>
"""


@PY.UBOT("capdl")
async def capcut_download(client, message):
    if len(message.command) < 2:
        await message.reply_text("Gunakan format: /capdl [URL CapCut]")
        return
    
    url = message.command[1]
    processing_msg = await message.reply_text("🔄 Memproses permintaan, harap tunggu...")
    
    response = requests.get(f"https://api.botcahx.eu.org/api/download/capcut?url={url}&apikey=moire")
    data = response.json()
    
    if not data.get("status"):
        await processing_msg.edit_text("❌ Gagal mengambil data. Pastikan URL valid.")
        return
    
    video_url = data["result"]["video"]
    thumbnail_url = data["result"]["thumbnail"]
    title = data["result"].get("short_title", "CapCut Video")
    author = data["result"].get("author", {}).get("name", "Unknown")
    
    await message.reply_video(
        video=video_url,
        thumb=thumbnail_url,
        caption=f"**{title}**\n👤 Pembuat: {author}\n🔗 [Sumber]({url})",
    )
    
    await processing_msg.delete()