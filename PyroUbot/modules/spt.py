from PyroUbot import *
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

SUPPORT = []

@PY.CALLBACK("^support")
async def support_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await client.get_users(user_id)
    await callback_query.message.delete()
    SUPPORT.append(get.id)
    try:
        button = [
            [InlineKeyboardButton("ʙᴀᴛᴀʟᴋᴀɴ", callback_data=f"batal {user_id}")]
        ]
        pesan = await client.ask(
            user_id,
            f"<b>ꜱɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴀɴᴅᴀ: {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=90,
        )
    except asyncio.TimeoutError as out:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return await client.send_message(get.id, "ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ")
    text = f"<b>ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴀɴᴅᴀ ꜱᴜᴅᴀʜ ᴛᴇʀᴋɪʀɪᴍ : {full_name}</b>"
    buttons = [
        [
            InlineKeyboardButton("👤 ᴘʀᴏꜰɪʟ", callback_data=f"profil {user_id}"),
            InlineKeyboardButton("ᴊᴀᴡᴀʙ 💬", callback_data=f"jawab_pesan {user_id}"),
        ],
    ]
    if get.id in SUPPORT:
        try:
            await pesan.copy(
                OWNER_ID,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(
                f"<b>ꜱɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴀɴᴅᴀ : {full_name}</b>"
            )
            return await client.send_message(user_id, text)
        except Exception as error:
            return await client.send_message(user_id, error)


@PY.CALLBACK("^jawab_pesan")
async def jawab_pesan_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await client.get_users(user_id)
    user_ids = int(callback_query.data.split()[1])
    SUPPORT.append(get.id)
    try:
        button = [
            [InlineKeyboardButton("ʙᴀᴛᴀʟᴋᴀɴ", callback_data=f"batal {user_id}")]
        ]
        pesan = await client.ask(
            user_id,
            f"<b>ꜱɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ʙᴀʟᴀꜱᴀɴ ᴀɴᴅᴀ: {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=300,
        )
    except asyncio.TimeoutError:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return await client.send_message(get.id, "ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ")
    text = f"<b>ꜱɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ʙᴀʟᴀꜱᴀɴ ᴀɴᴅᴀ : {full_name}</b>"
    if not user_ids == OWNER_ID:
        buttons = [[InlineKeyboardButton("💬 ᴊᴀᴡᴀʙ 💬", f"jawab_pesan {user_id}")]]
    else:
        buttons = [
            [
                InlineKeyboardButton("👤 ᴘʀᴏꜰɪʟ", callback_data=f"profil {user_id}"),
                InlineKeyboardButton("ᴊᴀᴡᴀʙ 💬", callback_data=f"jawab_pesan {user_id}"),
            ],
        ]
    if get.id in SUPPORT:
        try:
            await pesan.copy(
                user_ids,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(
                f"<b>ꜱɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ʙᴀʟᴀꜱᴀɴ ᴀɴᴅᴀ: {full_name}</b>",
            )
            await client.send_message(user_id, text)
        except Exception as error:
            return await client.send_message(user_id, error)


@PY.CALLBACK("^profil")
async def profil_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    try:
        get = await client.get_users(user_id)
        first_name = f"{get.first_name}"
        last_name = f"{get.last_name}"
        full_name = f"{get.first_name} {get.last_name or ''}"
        username = f"{get.username}"
        msg = (
            f"<b>👤 <a href=tg://user?id={get.id}>{full_name}</a></b>\n"
            f"<b> ┣ ɪᴅ ᴘᴇɴɢɢᴜɴᴀ:</b> <code>{get.id}</code>\n"
            f"<b> ┣ ɴᴀᴍᴀ ᴅᴇᴘᴀɴ:</b> {first_name}\n"
        )
        if last_name == "None":
            msg += ""
        else:
            msg += f"<b> ┣ ɴᴀᴍᴀ ʙᴇʟᴀᴋᴀɴɢɴʏᴀ:</b> {last_name}\n"
        if username == "None":
            msg += ""
        else:
            msg += f"<b> ┣ ᴜꜱᴇʀɴᴀᴍᴇ:</b> @{username}\n"
        msg += f"<b> ┗ bot: {client.me.mention}\n"
        buttons = [
            [
                InlineKeyboardButton(
                    f"{full_name}",
                    url=f"tg://openmessage?user_id={get.id}",
                )
            ]
        ]
        await callback_query.message.reply_text(
            msg, reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as why:
        await callback_query.message.reply_text(why)


@PY.CALLBACK("^batal")
async def batal_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    if user_id in SUPPORT:
        try:
            SUPPORT.remove(user_id)
            await callback_query.message.delete()
            buttons = BTN.START(callback_query)
            return await client.send_message(
                user_id,
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except Exception as why:
            await callback_query.message.delete()
            await client.send_message(user_id, f"<b>ɢᴀɢᴀʟ ᴅɪ ʙᴀᴛᴀʟᴋᴀɴ! {why}</b>")
