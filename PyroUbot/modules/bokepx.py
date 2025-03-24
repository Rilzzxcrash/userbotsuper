import random
from pyrogram.enums import MessagesFilter
from PyroUbot import *

__MODULE__ = "ʙᴏᴋᴇxx"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴏᴋᴇxx ⦫</b>

<blockquote><b>⎆ perintah :
ᚗ <code>{0}bokep1</code>
⊷ lagi nyari bokepnya bntr....

ᚗ <code>{0}bokep2</code>
⊷ lagi nyari bokepnya bntr....

ᚗ <code>{0}bokep3</code>
⊷ lagi nyari bokepnya bntr....
    
ᚗ <code>{0}bokep4</code>
⊷ lagi nyari bokepnya bntr....
    
ᚗ <code>{0}bokep5</code>
⊷ lagi nyari bokepnya bntr....</b></blockquote>
    
"""


@PY.UBOT("bokep1")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@vvideo_viral", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("bokep2")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupan18tocrot", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
        
@PY.UBOT("bokep3")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupan18tocrot", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
      
@PY.UBOT("bokep4")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupan18tocrot", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
        
@PY.UBOT("bokep5")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupan18tocrot", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)