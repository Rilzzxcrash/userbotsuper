import random
from pyrogram.enums import MessagesFilter
from PyroUbot import *

__MODULE__ = "ᴀꜱᴜᴘᴀɴ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ ⦫</b>

<blockquote><b>⎆ perintah :
ᚗ <code>{0}asupan</code>
⊷ mengirim video asupan random 

ᚗ <code>{0}cewek</code>
⊷ mengirim photo cewe random

ᚗ <code>{0}cowok</code>
⊷ mengirim photo cowo random</b></blockquote>  
"""


@PY.UBOT("asupan")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}mencari video asupan...")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("cewek")
@PY.TOP_CMD
async def photo_cewek(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}mencari ayang...")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
