import asyncio
import random

from PyroUbot import *

@PY.UBOT("cekkontol|cekkntl")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ᴋᴏɴᴛᴏʟ {nama} </b>
<blockquote><b>╭───「 ʜᴀsɪʟ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ 」───</b>
<b>┆• ᴡᴀʀɴᴀ ᴋᴏɴᴛᴏʟ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴜᴋᴜʀᴀɴ ᴋᴏɴᴛᴏʟ : {pick_random(['16 cm', '10 cm', '15 cm', '6 cm', '1 cm', '3 cm'])}</b>
<b>┆• ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {pick_random(['bengkok', 'bengkok dikit', 'lurus', 'panjang kecil', 'lebar', 'tumpul'])}</b>
<b>╰──────────────────────</b></blockquote>
  <b>ɴᴇxᴛ ᴄᴇᴋ ᴋᴏɴᴛᴏʟɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.</b>   
      """
        await message.edit(hasil)
    except BaseException:
        pass

@PY.UBOT("cekmemek|cekmmk")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ᴍᴇᴍᴇᴋ {nama} </b>
<blockquote><b>╭───「 ʜᴀsɪʟ ᴄᴇᴋ ᴍᴇᴍᴇᴋ 」───</b>
<b>┆• ᴡᴀʀɴᴀ ᴍᴇᴍᴇᴋ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴜᴋᴜʀᴀɴ ʟᴏʙᴀɴɢ : {pick_random(['16 inc', '10 inc', '15 inc', '6 inc', '1 inc', '3 inc'])}</b>
<b>┆• ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {pick_random(['berjembut', 'dah jebol', 'bau trasi', 'berlendir', 'lebar itam', 'sempit'])}</b>
<b>╰──────────────────────</b></blockquote>
  <b>ɴᴇxᴛ ᴄᴇᴋ ᴍᴇᴍᴇᴋɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.</b>   
      """
        await message.edit(hasil)
    except BaseException:
        pass

@PY.UBOT("ceksange|ceksagne")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ sᴀɴɢᴇ</b>
<blockquote><b>╭───「 ʜᴀsɪʟ ᴄᴇᴋ sᴀɴɢᴇ 」───</b>
<b>┆• ɴᴀᴍᴀ :  {nama} </b>
<b>┆• sᴀɴɢᴇ : {pick_random(['90%', '95%', '75%', '85%', '100%'])}</b>
<b>┆• sᴀɴɢᴇᴀɴ ᴋᴏɴᴛᴏʟ </b>
<b>╰──────────────────────</b></blockquote>
  <b>ɴᴇxᴛ ᴄᴇᴋ sᴀɴɢᴇ sɪᴀᴘᴀ ʟᴀɢɪ.</b>   
      """
        await message.edit(hasil)
    except BaseException:
        pass
__MODULE__ = "ᴄᴇᴋ ᴄɪʀɪ"
__HELP__ = """<b>「 BANTUAN UNTUK MODULE CEK CIRI 」</b>

<b>𖠇➛ ᴘᴇʀɪɴᴛᴀʜ: .cekkontol</b>
<b>𖠇➛ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴇᴋ ᴋᴏɴᴛᴏʟ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ ᴏʀᴀɴɢɴʏᴀ</b>

<b>𖠇➛ ᴘᴇʀɪɴᴛᴀʜ: .cekmemek</b>
<b>𖠇➛ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴇᴋ ᴍᴇᴍᴇᴋ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ ᴏʀᴀɴɢɴʏᴀ</b>

<b>𖠇➛ ᴘᴇʀɪɴᴛᴀʜ: .ceksange</b>
<b>𖠇➛ ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴄᴇᴋ sᴀɴɢᴇ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ ᴏʀᴀɴɢɴʏᴀ</b>
  """
