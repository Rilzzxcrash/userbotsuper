import os
import requests
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "Upload MediaFire"
__HELP__ = """
<blockquote><b>Bantuan Untuk Upload MediaFire</b>

Perintah:
<code>.mediafire</code> → Mengunggah file ZIP ke MediaFire.

Balas perintah ini dengan file ZIP.</blockquote></b>
"""

# Ganti dengan API Key & Email MediaFire (jika ada)
MEDIAFIRE_EMAIL = "zamsswangsaff@gmail.com"
MEDIAFIRE_PASSWORD = "Nizam20@"

@PY.UBOT("mediafire")
@PY.TOP_CMD
async def _(client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply_text("❌ Silakan reply file ZIP untuk diunggah!")

    msg = await message.reply_text("🔄 Mengunggah file ke MediaFire...")

    # Ambil informasi file
    file = message.reply_to_message.document
    file_path = await client.download_media(file)

    if not file_path.endswith(".zip"):
        return await msg.edit("❌ Hanya file ZIP yang bisa diunggah!")

    try:
        # Login ke MediaFire
        login_url = "https://www.mediafire.com/api/1.5/user/get_session_token.php"
        login_params = {
            "email": MEDIAFIRE_EMAIL,
            "password": MEDIAFIRE_PASSWORD,
            "application_id": "42511",  # ID aplikasi MediaFire
            "response_format": "json"
        }
        login_response = requests.get(login_url, params=login_params).json()
        
        if login_response["response"]["result"] != "Success":
            return await msg.edit("❌ Gagal login ke MediaFire!")

        session_token = login_response["response"]["session_token"]

        # Upload file
        upload_url = "https://www.mediafire.com/api/1.5/upload/simple.php"
        upload_params = {
            "session_token": session_token,
            "response_format": "json"
        }
        files = {"file": open(file_path, "rb")}
        upload_response = requests.post(upload_url, params=upload_params, files=files).json()
        
        if upload_response["response"]["result"] != "Success":
            return await msg.edit("❌ Gagal mengunggah file!")

        file_link = upload_response["response"]["doupload"]["links"]["normal_download"]
        
        await msg.edit(f"✅ **Berhasil diunggah!**\n🔗 [Download di MediaFire]({file_link})")
    
    except Exception as e:
        await msg.edit(f"❌ Terjadi kesalahan: {str(e)}")

    finally:
        os.remove(file_path)  # Hapus file lokal setelah diunggah