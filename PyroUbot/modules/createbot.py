from pyrogram import Client, filters
from PyroUbot import PY
from PyroUbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ ʙᴏᴛ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Auto Create Bot</b>

Perintah: <code>{0}createbot</code> [nama_bot username_bot]
Penjelasan: Membuat bot Telegram baru secara otomatis melalui @BotFather</blockquote></b>
"""

@PY.UBOT("createbot")
@PY.TOP_CMD
async def create_bot_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.reply_text(
            "<blockquote><b>⚠️ Gunakan format: createbot [nama_bot] [username_bot]</b></blockquote>\n"
            "Contoh: <code>.createbot MyNewBot MyNew_Bot</code>"
        )
        return

    bot_name = args[1]
    bot_username = args[2]

    if not bot_username.endswith("Bot"):
        await message.reply_text("❌ **Username bot harus diakhiri dengan 'Bot'.**")
        return

    try:
        botfather = "@BotFather"
        
        # Kirim perintah ke BotFather
        await client.send_message(botfather, "/newbot")
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_name)
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_username)

        await message.reply_text(
            f"<blockquote><b>✅ **Permintaan pembuatan bot telah dikirim ke @BotFather!**\n"
            f"🆕 **Nama Bot:** `{bot_name}`\n"
            f"🔗 **Username:** @{bot_username}\n\n"
            "Silakan cek @BotFather untuk melanjutkan proses konfigurasi.</blockquote></b>"
        )
    
    except Exception as e:
        await message.reply_text(f"⚠️ Terjadi kesalahan: {str(e)}")