
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot.core.helpers.msg_type import ReplyCheck
from PyroUbot import *

@ubot.on_message(filters.command("unprem") & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ"
__HELP__ = f"""
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ ⦫</b>

<blockquote><b>⎆ perintah : <code>/ʙᴄ</code>
ᚗ  ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ʟᴇᴡᴀᴛ ʙᴏᴛ
"""

@PY.BOT("bc")
@PY.OWNER
async def broadcast_bot(client, message):
    msg = await message.reply("<b>⌭ sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>", quote=True)
    done = 0
    if not message.reply_to_message:
        return await msg.edit("<b>⌭ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴘᴇsᴀɴ</b>")
    for x in ubot._ubot:
        try:
            await x.unblock_user(bot.me.username)
            await message.reply_to_message.forward(x.me.id)
            done += 1
        except Exception:
            pass
    return await msg.edit(f"⌭ ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ {done} ᴜʙᴏᴛ")
