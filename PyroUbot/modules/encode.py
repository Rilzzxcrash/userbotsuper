import os
import subprocess
from pyrogram import Client, filters
from PyroUbot import PY
import shutil
from pyrogram.types import Message

__MODULE__ = "ᴇɴᴄʀʏᴘᴛ ʜᴀʀᴅ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Encrypt JS</b>

Perintah:
<code>{0}enc</code> → Balas file .js untuk dienkripsi.

Sumber: Menggunakan UglifyJS untuk enkripsi JavaScript.</blockquote></b>
"""

# Periksa apakah UglifyJS sudah terinstal
if not shutil.which("uglifyjs"):
    raise Exception("⚠️ UglifyJS belum terinstal. Install dengan `npm install -g uglify-js`")

@PY.UBOT("enc")
@PY.TOP_CMD
async def encrypt_js(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply("😠 Silakan balas file .js untuk dienkripsi.")

    file_info = message.reply_to_message.document
    file_name = file_info.file_name

    if not file_name.endswith('.js'):
        return await message.reply("❌ File harus berekstensi .js!")

    msg = await message.reply("⚡ Mengunduh file...")
    input_path = await client.download_media(message.reply_to_message.document)
    output_path = f"./encrypted_{file_name}"

    await msg.edit("⚡ Melakukan hard obfuscation dengan JsConfuser...")

    try:
        subprocess.run(
            ["node", "confuser.js", input_path, output_path],
            check=True
        )
        await message.reply_document(
            output_path,
            caption="✅ **File berhasil di-obfuscate!**\n🔒 Menggunakan JsConfuser Unicode"
        )
    except subprocess.CalledProcessError:
        await msg.edit("❌ Gagal melakukan hard encrypt!")

    # Cleanup
    os.remove(input_path)
    if os.path.exists(output_path):
        os.remove(output_path)
