import asyncio
import random

from PyroUbot import *

__MODULE__ = "ᴄᴇᴋɢᴀɴᴛᴇɴɢ"
__HELP__ = """**「 BANTUAN UNTUK MODULE CEK GANTENG 」**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .cekganteng**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɢᴀɴᴛᴇɴɢ ɴᴀᴍᴀ ᴏʀᴀɴɢ**"""


@PY.UBOT("cekganteng")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
 <b>𖤐 ʜᴀsɪʟ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ:</b>
╭───────────────────────
├ •ɴᴀᴍᴀ : {nama}
├ •ɢᴀɴᴛᴇɴɢ : {pick_random(['ᴋᴀʏᴀ ᴋᴛʟ', 'ᴅɪᴋɪᴛ', 'ʙᴀɴʏᴀᴋ', 'sᴇᴛᴇɴɢᴀʜ', 'sᴇᴘᴇʀᴀᴘᴀᴛ', 'sᴇ ᴛᴇᴛᴇ'])}
├ •ɴɢᴇʀɪ ʙᴇᴛ ᴊɪʀ
╰────────────────────────
  **ɴᴇxᴛ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ sɪᴀᴘᴀ ʟᴀɢɪ.**       
      """
        await message.edit(hasil)
    except BaseException:
        pass
