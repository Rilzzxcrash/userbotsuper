import requests
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ᴀᴛᴛᴘ-ᴛᴛᴘ"
__HELP__ = """
<blockquote><b>『 ᴀᴛᴛᴘ & ᴛᴛᴘ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> 
    ◉ <code>{0}attp</code> <i>teks</i> - Membuat stiker teks berwarna.
    ◉ <code>{0}ttp</code> <i>teks</i> - Membuat stiker teks biasa.</blockquote>
"""

API_KEY = "moire"

@PY.UBOT("attp")
async def attp(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} Sedang memproses...")
    
    try:
        # Ambil teks dari perintah
        args = message.text.split(' ', 1)
        if len(args) < 2:
            await jalan.edit(f"{ggl} Harap masukkan teks! Contoh: <code>!attp Halo</code>")
            return
        
        text = args[1]
        # URL API untuk ATTP
        url = f"https://api.botcahx.eu.org/api/maker/attp?text={text}&apikey={API_KEY}"
        
        # Kirim permintaan ke API
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Simpan file sementara untuk dikirim
            with open("attp.webp", "wb") as file:
                file.write(response.content)
            
            # Kirim sebagai animasi (stiker animasi)
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker="attp.webp",
                reply_to_message_id=message.id
            )
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} Gagal mendapatkan stiker ATTP. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Permintaan gagal: {e}")
    except Exception as e:
        await jalan.edit(f"{ggl} Terjadi kesalahan: {e}")

@PY.UBOT("ttp")
async def ttp(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"{prs} Sedang memproses...")
    
    try:
        # Ambil teks dari perintah
        args = message.text.split(' ', 1)
        if len(args) < 2:
            await jalan.edit(f"{ggl} Harap masukkan teks! Contoh: <code>!ttp Halo</code>")
            return
        
        text = args[1]
        # URL API untuk TTP
        url = f"https://api.botcahx.eu.org/api/maker/ttp?text={text}&apikey={API_KEY}"
        
        # Kirim permintaan ke API
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Simpan file sementara untuk dikirim
            with open("ttp.webp", "wb") as file:
                file.write(response.content)
            
            # Kirim sebagai stiker
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker="ttp.webp",
                reply_to_message_id=message.id
            )
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} Gagal mendapatkan stiker TTP. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Permintaan gagal: {e}")
    except Exception as e:
        await jalan.edit(f"{ggl} Terjadi kesalahan: {e}")
