import os
from PyroUbot import *
import requests

__MODULE__ = "sᴛᴀʙʟᴇᴅɪғғᴜsɪᴏɴ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʙʟᴇᴅɪғғᴜsɪᴏɴ ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}sd</code> text
⊶ Untuk Membuat Gambar Menggunakan Text.</b></blockquote>
"""

def get_giraffe_image(text):
    url = "https://api.botcahx.eu.org/api/search/stablediffusion"
    params = {
        "text": text,
        "apikey": f"moire"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
                                                       
@PY.UBOT("sd")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("<b><i>Gunakan perintah /stablediffusion <teks> untuk membuat gambar</i></b>.")
        return

    request_text = args[1]
    await message.reply_text("<b><i>Sedang memproses, mohon tunggu</i></b>...")

    image_content = get_giraffe_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("Gagal membuat gambar. Coba lagi nanti.")