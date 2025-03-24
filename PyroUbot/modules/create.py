from PyroUbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ ᴄʜ/ɢʙ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʀᴇᴀᴛᴇ ᴄʜ/ɢʙ ⦫</b>
<blockquote>
⎆ perintah :
ᚗ <code>{0}create</code> group nama
ᚗ <code>{0}create</code> channel nama

⎆ ᴘᴇɴᴊᴇʟᴀsᴀɴ:
⊶ Membuat Chanel atau Group Telegram
</blockquote>
"""
@PY.UBOT("create")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"{message.text} [group/channel] [name/titlee]")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("memproꜱeꜱ...")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram grup: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram channel: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
