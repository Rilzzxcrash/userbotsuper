from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴀsᴠɪʀ ᴀɪ"
__HELP__ = """
<blockquote><b>✮ Bantuan Untuk Asisten Virtual ✮

perintah : <code>{0}asvir</code>
    ai bisa digunakan untuk:translate,memberikan saran,membuat text , contoh <code>{0}asvir</code> bahasa ingris nya 'siapa kamu' itu apa?</b></blockquote>
"""

@PY.UBOT("asvir")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .asvir bahasa ingris nya 'siapa kamu' itu apa?"
            )
        else:
            prs = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji>Menjawab....")
            hai = message.text.split(' ', 1)[1]
            response = requests.get(f'https://vapis.my.id/api/llamav1?q={hai}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
      
