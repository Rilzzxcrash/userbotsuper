from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴀʀᴛɪ ɴᴀᴍᴀ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Arti Nama</b>

Perintah:
<code>{0}artinama [nama]</code> → Mengartikan dengan nama</blockquote></b>
"""

@PY.UBOT("artinama")
async def _(client, message):
    if len(message.command) < 2:
        await message.reply_text("<blockquote><b>**Gunakan perintah:** `/artinama nama`\n\nContoh: `/artinama putu`</blockquote></b>")
        return

    nama = " ".join(message.command[1:])
    api_url = f"https://api.siputzx.my.id/api/primbon/artinama?nama={nama}"

    try:
        response = requests.get(api_url).json()

        if response.get("status"):
            nama_res = response["data"]["nama"].title()
            arti_res = response["data"]["arti"]
            catatan_res = response["data"].get("catatan", "")

            reply_text = (
                f"<blockquote><b>**🔍 Arti Nama: {nama_res}**\n\n</blockquote></b>"
                f"<blockquote><b>📖 {arti_res}\n</blockquote></b>"
            )

            if catatan_res:
                reply_text += f"<blockquote><b>\n💡 *{catatan_res}*</blockquote></b>"

            await message.reply_text(reply_text)
        else:
            await message.reply_text(f"<blockquote><b>❌ Maaf, arti nama **{nama}** tidak ditemukan.</blockquote></b>")
    except Exception as e:
        await message.reply_text(f"<blockquote><b>⚠️ Terjadi kesalahan saat mengambil data:\n`{str(e)}`</blockquote></b>")