import asyncio
import random

from PyroUbot import *

__MODULE__ = "ᴄᴇᴋᴄᴀɴᴛɪᴋ"
__HELP__ = """**「 BANTUAN UNTUK MODULE CEK CANTIK 」**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .cekcantik**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀɴᴛɪᴋ ɴᴀᴍᴀ ᴏʀᴀɴɢ**"""


@PY.UBOT("cekcantik")
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
 <b>𖤐 ʜᴀsɪʟ ᴄᴇᴋ ᴄᴀɴᴛɪᴋ:</b>
╭───────────────────────
├ •ɴᴀᴍᴀ : {nama}
├ •ᴄᴀɴᴛɪᴋ : {pick_random(['ɢᴀ sᴇʙᴇʀᴀᴘᴀ', 'ᴅɪᴋɪᴛ', 'ʙᴀɴʏᴀᴋ', 'sᴇᴛᴇɴɢᴀʜ', 'sᴇᴘᴇʀᴀᴘᴀᴛ', 'sᴇ ᴛᴇᴛᴇ'])}
├ •ɴɢᴇʀɪ ʙᴇᴛ ᴊɪʀ
╰────────────────────────
  **ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ.**       
      """
        await message.edit(hasil)
    except BaseException:
        pass
