from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from PyroUbot import *
import time

__MODULE__ = "ʙᴜᴛᴛᴏɴ"
__HELP__ = """
<b>⦪ ʙᴜᴛᴛᴏɴ ⦫</b>

<blockquote><b>⎆  ᴘᴇʀɪɴᴛᴀʜ:
ᚗ <code>{0}button</code> ᴛᴇxᴛ -/ ʙᴜᴛᴛᴏɴ_ᴛᴇxᴛ:ʟɪɴᴋ [| ʙᴜᴛᴛᴏɴ_ʟᴀɪɴ:ʟɪɴᴋ]
ᚗ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴏᴍʙᴏʟ ɪɴʟɪɴᴇ</b></blockquote>
"""

# Simpan data sementara
CACHE_BUTTONS = {}


def clean_cache():
    now = int(time.time())
    expired = [k for k, v in CACHE_BUTTONS.items() if now - int(k.split("_")[1]) > 300]
    for k in expired:
        del CACHE_BUTTONS[k]


@PY.UBOT("button")
async def cmd_button(client, message):
    if len(message.command) < 2 or "-/" not in message.text:
        return await message.reply(
            "Contoh penggunaan:\n<code>.button Teks utama -/ Nama Tombol:Link</code>\n"
            "Ketik <code>.help button</code> untuk info lebih lanjut."
        )

    clean_cache()

    try:
        # Pisahkan teks dan tombol
        text_part, button_part = message.text.split("-/", 1)
        text = text_part.strip().split(None, 1)[1]
        buttons = []
        for btn in button_part.strip().split("|"):
            btn_text, btn_url = btn.strip().split(":", 1)
            buttons.append([InlineKeyboardButton(btn_text.strip(), url=btn_url.strip())])
    except Exception as e:
        return await message.reply(f"Format salah: {e}")

    # Buat ID unik
    query_id = str(message.id) + "_" + str(int(time.time()))
    CACHE_BUTTONS[query_id] = (text, InlineKeyboardMarkup(buttons))

    await message.delete()
    try:
        results = await client.get_inline_bot_results(bot.me.username, f"get_button {query_id}")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, results.query_id, results.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(f"❌ Gagal: {error}")


@PY.INLINE("^get_button")
async def inline_button(client, inline_query):
    try:
        query_id = inline_query.query.split(None, 1)[1].strip()
        text, buttons = CACHE_BUTTONS[query_id]
    except Exception:
        return await inline_query.answer(
            [],
            cache_time=1,
            switch_pm_text="❌ Tombol tidak ditemukan.",
            switch_pm_parameter="start"
        )

    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Kirim tombol ini",
                input_message_content=InputTextMessageContent(text),
                reply_markup=buttons,
                description="Klik untuk mengirim ke chat"
            )
        ],
        cache_time=0
    )
