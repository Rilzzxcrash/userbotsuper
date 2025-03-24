from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴀɴɪᴍᴇ 2"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴇ 2 ⦫</b>
<blockquote>
⎆ perintah :
ᚗ <code>{0}anime</code> Query
⊶ buat pertanyaan contoh <code>{0}ask</code> dimana letak Antartika

<b>ᚗ Query:</b>
    <i>⊶ keneki</i>,
    <i>⊶ megumin/i>,
    <i>⊶ yotsuba</i>,
    <i>⊶ shinomiya</i>,
    <i>⊶ yumeko</i>,
    <i>⊶ tsunade</i>,
    <i>⊶ kagura</i>,
    <i>⊶ madara</i>,
    <i>⊶ itachi</i>,
    <i>⊶ akira</i>,
    <i>⊶ toukachan</i>,
    <i>⊶ cicho</i>,
    <i>⊶ sasuke</i></blockquote>
"""

URLS = {
    "keneki": "https://api.botcahx.eu.org/api/anime/keneki?apikey=moire",
    "megumin": "https://api.botcahx.eu.org/api/anime/megumin?apikey=moire",
    "yotsuba": "https://api.botcahx.eu.org/api/anime/yotsuba?apikey=moire",
    "shinomiya": "https://api.botcahx.eu.org/api/anime/shinomiya?apikey=moire",
    "yumeko": "https://api.botcahx.eu.org/api/anime/yumeko?apikey=moire",
    "tsunade": "https://api.botcahx.eu.org/api/anime/tsunade?apikey=moire",
    "kagura": "https://api.botcahx.eu.org/api/anime/kagura?apikey=moire",
    "madara": "https://api.botcahx.eu.org/api/anime/madara?apikey=moire",
    "itachi": "https://api.botcahx.eu.org/api/anime/itachi?apikey=moire",
    "akira": "https://api.botcahx.eu.org/api/anime/akira?apikey=moire",
    "toukachan": "https://api.botcahx.eu.org/api/anime/toukachan?apikey=moire",
    "cicho": "https://api.botcahx.eu.org/api/anime/chiho?apikey=moire",
    "sasuke": "https://api.botcahx.eu.org/api/anime/sasuke?apikey=moire"
}

@PY.UBOT("anime")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing....")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar anime Error: {e}")
