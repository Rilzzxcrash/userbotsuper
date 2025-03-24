from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴄᴇᴄᴀɴ"
__HELP__ = """
📚 <b>--Folder Untuk Cecan--</b>

<blockquote><b>🚦 Perintah : <code>{0}cecan [query]</code>
🦠 Penjelasan : Mengirim Foto Random Sesuai Query.</b></blockquote>
<blockquote><b>📖 Penggunaan : 
 Query: 
    Indonesia,
    china,
    thailand,
    vietnam,
    waifu,
    neko,
    shinobu,
    hubble,
    malaysia,
    japan,
    korea</b></blockquote>
"""

URLS = {
    "indonesia": "https://widipe.com/indonesia",
    "china": "https://widipe.com/china",
    "thailand": "https://widipe.com/thailand",
    "vietnam": "https://widipe.com/vietnam",
    "waifu": "https://widipe.com/waifu",
    "neko": "https://widipe.com/neko",
    "shinobu": "https://widipe.com/shinobu",
    "hubble": "https://widipe.com/hubbleimg",
    "malaysia": "https://widipe.com/malaysia",
    "japan": "https://widipe.com/japan",
    "korea": "https://widipe.com/korea"
}

@PY.UBOT("cecan")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar cecan Error: {e}")
