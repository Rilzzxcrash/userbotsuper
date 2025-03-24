from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴅᴜᴋᴜɴ ᴀɪ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Dukun Ai

perintah : <code>{0}dukunai</code>
meramal dengan nama/peristiwa contoh <code>{0}dukunai</code> namaku boysz</b></blockquote>
"""

@PY.UBOT("dukunai")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .dukunai namaku fxyy"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5192886773948107844>😮‍💨</emoji>Mbah Dukun Sedang Meramal....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.siputzx.my.id/api/ai/dukun?content={a}')

            try:
                if "data" in response.json():
                    x = response.json()["data"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
