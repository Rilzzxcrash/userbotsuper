import asyncio
import os
import re

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from PyroUbot import *
from PyroUbot.core.database import mongo_client

__MODULE__ = "ᴀɴᴛɪɢᴄᴀsᴛ"
__HELP__ = """

<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴᴛɪɢᴄᴀsᴛ ⦫</b>
<blockquote><b>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}on</code> [on atau off] 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜɪᴅᴜᴘᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇᴍᴀᴛɪᴋᴀɴ ᴀɴᴛɪɢᴄᴀꜱᴛ

ᚗ <code>{0}listduar</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪ ʙᴀʟᴄᴋʟɪꜱᴛ

ᚗ <code>{0}duar</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜ ᴘᴇɴɢɢᴜɴᴀ ᴋᴇ ᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀꜱᴇ ᴀɴᴛɪɢᴄᴀꜱᴛ

ᚗ <code>{0}unduar</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴘᴇɴɢɢᴜɴᴀ ᴅɪ ᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀꜱᴇ ᴀɴᴛɪɢᴄᴀꜱᴛ

ᚗ <code>{0}liat</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴀᴘᴀᴋᴀʜ ᴀɴᴛɪɢᴄᴀꜱᴛ ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪꜰᴋᴀɴ

ᚗ <code>{0}addgc</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜ ɢʀᴜᴘ ꜱᴇʙᴀɢᴀɪ ᴀɴᴛɪɢᴄᴀꜱᴛ

ᚗ <code>{0}rmgc</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ɢʀᴜᴘ ꜱᴇʙᴀɢᴀɪ ᴀɴᴛɪɢᴄᴀꜱᴛ

ᚗ <code>{0}listgc</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɢʀᴜᴘ ᴀɴᴛɪɢᴄᴀꜱᴛ</b></i>

ᚗ <code>{0}b</code> balas ke pesan 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜ ᴘᴇꜱᴀɴ ᴀɴᴛɪɢᴄᴀꜱᴛ

ᚗ <code>{0}cekbl</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ ᴅᴀꜰᴛᴀʀ ᴋᴀᴛᴀ ʏɢ ᴅɪ ʙʟᴀᴄᴋʟɪꜱᴛ

ᚗ <code>{0}rmb</code> 
⊷ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪ ʙʟᴀᴄᴋʟɪꜱᴛ
</b></blockquote>

"""

db = mongo_client["DOR"]
user_collection = db["user_dia"]
gc = db["listgrup"]
psnz = db["msg_text"]


async def get_user_ids(client_id):
    user_ids = await user_collection.find_one({"_id": client_id})
    return user_ids["user_dia"] if user_ids else []


async def get_blacklist_status(client_id):
    blacklist_status = await db.settings.find_one({"_id": client_id})
    return blacklist_status["status"] if blacklist_status else False


async def set_blacklist_status(client_id, status):
    await db.settings.update_one({"_id": client_id}, {"$set": {"status": status}}, upsert=True)


async def get_chat_ids(client_id):
    chat_ids = await gc.find_one({"_id": client_id})
    return chat_ids["grup"] if chat_ids else []


async def get_msg_ids(client_id):
    msg_ids = await psnz.find_one({"_id": client_id})
    return msg_ids["msg_text"] if msg_ids else []


async def purge(message):
    await asyncio.sleep(0.5)
    await message.delete()


def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else "" if len(message.command) < 2 else " ".join(message.command[1:])
    )
    return msg


def emoji(alias):
    emojis = {
        "bintang": "<emoji id=5931592939514892319>⭐</emoji>",
        "loading": "<emoji id=5801044672658805468>✨</emoji>",
        "proses": "<emoji id=6276248783525251352>🔄</emoji>",
        "gagal": "<emoji id=6278161560095426411>❌</emoji>",
        "done": "<emoji id=5852871561983299073>✅</emoji>",
        "upload": "<emoji id=5911100572508885928>♻️</emoji>",
        "roses": "<emoji id=5341312820698948923>🙃</emoji>",
        "selesai": "<emoji id=5341576484446283436>😎</emoji>",
        "on": "<emoji id=6275808772715710450>🎚️</emoji>",
        "off": "<emoji id=6276295366740543459>⛔</emoji>",
        "daftar": "<emoji id=5974045315391556490>📝</emoji>",
    }
    return emojis.get(alias, "Emoji tidak ditemukan.")


Q = emoji("bintang")
gagal = emoji("gagal")
prs = emoji("proses")
batal = emoji("gagal")
rs = emoji("roses")
sls = emoji("selesai")
dn = emoji("done")
on = emoji("on")
off = emoji("off")
dftr = emoji("daftar")


@PY.UBOT("duar")
@PY.TOP_CMD
async def add_user_to_blacklist(c, m):
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(
            f"{batal}**gunakan format** : `duar` **user id atau balas ke pesan untuk menambahkan ke daftar antigcast {Q}**",
            quote=True,
        )
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        try:
            user_id = int(m.command[1])
        except ValueError:
            try:
                user = await c.get_users(m.command[1])
                user_id = user.id
            except Exception:
                await m.reply_text(f"{gagal} Tidak dapat menemukan pengguna dengan username {m.command[1]}", quote=True)
                return

    user_ids = await get_user_ids(c.me.id)
    if user_id not in user_ids:
        user_ids.append(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"{Q}**user dengan id** `{user_id}` **telah ditambahkan ke daftar antigcast** {dn}", quote=True)
    else:
        await m.reply_text(f"{dn}**user tersebut sudah ada dalam daftar antigcast {Q}**", quote=True)


@PY.UBOT("listduar")
@PY.TOP_CMD
async def display_blacklist(client, message):
    user_ids = await get_user_ids(client.me.id)
    await message.reply_text(f"{dftr} ini hasilnya : `{user_ids}`\n", quote=True)


@PY.UBOT("unduar")
@PY.TOP_CMD
async def remove_user_from_blacklist(c, m):
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(
            f"{batal}**gunakan format** : `unduar` **user id atau balas ke pesan untuk menghapus dari daftar antigcast {Q}**",
            quote=True,
        )
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    user_ids = await get_user_ids(c.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"{Q}**user dengan id** `{user_id}` **telah dihapus dalam daftar antigcast** {dn}", quote=True)
    else:
        await m.reply_text(f"{Q}**user tersebut tidak ada dalam daftar antigcast {gagal}**", quote=True)


@PY.UBOT("liat")
@PY.TOP_CMD
async def checkstatus(client, message):
    cek = await get_blacklist_status(client.me.id)
    if cek:
        await message.reply_text(f"{Q}**anda sudah mengaktifkan antigcast**{dn}", quote=True)
    else:
        await message.reply_text(f"{Q}**anda belum mengaktifkan antigcast**{gagal}", quote=True)


@PY.UBOT("on")
@PY.TOP_CMD
async def enable_blacklist(c, m):
    await set_blacklist_status(c.me.id, True)
    await m.reply_text(f"{Q}**antigcast user berhasil di aktifkan** {on}", quote=True)


@PY.UBOT("off")
@PY.TOP_CMD
async def disable_blacklist(c, m):
    await set_blacklist_status(c.me.id, False)
    await m.reply_text(f"{Q}**antigcast user berhasil di matikan** {off}", quote=True)


@PY.UBOT("addgc")
@PY.TOP_CMD
async def add_group_to_antigcast(c, m):
    type = (ChatType.GROUP, ChatType.SUPERGROUP)

    if m.chat.type not in type:
        await m.reply_text(f"{gagal}gunakan fitur ini di grup!")
        return

    user_id = m.chat.id
    chat_ids = await get_chat_ids(c.me.id)
    if user_id not in chat_ids:
        chat_ids.append(user_id)
        await gc.update_one({"_id": c.me.id}, {"$set": {"grup": chat_ids}}, upsert=True)
        await m.reply_text(f"{Q}**grup dengan id** `{user_id}` **telah ditambahkan ke daftar antigcast** {dn}", quote=True)
    else:
        await m.reply_text(f"{dn}**grup tersebut sudah ada dalam daftar antigcast {Q}**", quote=True)


@PY.UBOT("rmgc")
@PY.TOP_CMD
async def remove_group_from_antigcast(c, m):
    type = (ChatType.GROUP, ChatType.SUPERGROUP)
    if m.chat.type not in type:
        await m.reply_text(f"{gagal} Gunakan fitur ini di grup atau berikan ID grup", quote=True)
        return

    chat_id = None
    if len(m.command) >= 2:
        try:
            chat_id = int(m.command[1])
        except ValueError:
            await m.reply_text(f"{gagal} ID grup tidak valid", quote=True)
            return

    if not chat_id:
        chat_id = m.chat.id

    chat_ids = await get_chat_ids(c.me.id)
    if chat_id in chat_ids:
        chat_ids.remove(chat_id)
        await gc.update_one({"_id": c.me.id}, {"$set": {"grup": chat_ids}}, upsert=True)
        await m.reply_text(f"{Q} Grup dengan ID {chat_id} telah dihapus dari daftar antigcast {dn}", quote=True)
    else:
        await m.reply_text(f"{Q} Grup dengan ID {chat_id} tidak ada dalam daftar antigcast {gagal}", quote=True)


@PY.UBOT("listgc")
@PY.TOP_CMD
async def display_antigcast(c, m):
    user_ids = await get_chat_ids(c.me.id)
    await m.reply_text(f"{dftr}**daftar grup antigcast** : `{user_ids}` \n", quote=True)


@PY.UBOT("b")
@PY.TOP_CMD
async def add_pesan(c, m):
    _rply = m.reply_to_message
    if not _rply:
        await m.reply(f"mohon balas ke pengguna")
        return
    user_text = _rply.text
    msg_ids = await get_msg_ids(c.me.id)
    if user_text not in msg_ids:
        msg_ids.append(user_text)
        await psnz.update_one({"_id": c.me.id}, {"$set": {"msg_text": msg_ids}}, upsert=True)
        sukses = await m.reply_text(f"pesan {user_text} berhasil di tambahkan ke database{dn}", quote=True)
        await _rply.delete()
        await purge(m)
        await sukses.delete()
    else:
        x = await m.reply_text(f"pesan sudah ada di dalam database{gagal}", quote=True)
        await asyncio.sleep(0.5)
        await x.delete()


@PY.UBOT("cekbl")
@PY.TOP_CMD
async def strdb(client, message):
    pesan = await get_msg_ids(client.me.id)
    try:
        await message.reply_text(pesan)
    except MessageTooLong:
        with open("db.txt", "a", encoding="utf-8") as file:
            file.write(f"{pesan}\n")
        kirim = await message.reply_document(db.txt)
        if kirim:
            os.remove("db.txt")


@PY.UBOT("rmb")
@PY.TOP_CMD
async def remove_kata_from_blacklist(c, m):
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(
            f"{batal}**gunakan format** : `rmkat` **user id atau balas ke pesan untuk menghapus dari daftar antigcast {Q}**",
            quote=True,
        )
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.text
    else:
        user_id = " ".join(m.command[1:])

    user_ids = await get_msg_ids(c.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await psnz.update_one({"_id": c.me.id}, {"$set": {"msg_text": user_ids}}, upsert=True)
        await m.reply_text(f"{Q}**berhasil menghapus** `{user_id}` **dari daftar kata antigcast** {dn}", quote=True)
    else:
        await m.reply_text(f"{Q}**kata tersebut tidak ada dalam daftar antigcast {gagal}**", quote=True)


@ubot.on_message(filters.group & ~filters.me, group=75)
async def delete_messages(client, message):
    try:
        chat_ids = await get_chat_ids(client.me.id)
        if message.chat.id not in chat_ids:
            return

        blacklist_status = await get_blacklist_status(client.me.id)
        if not blacklist_status:
            return

        user_ids = await get_user_ids(client.me.id)
        user_msg_patterns = await get_msg_ids(client.me.id)

        if message.from_user.id in user_ids:
            return await message.delete()
        else:
            for pattern in user_msg_patterns:
                if bool(re.search(pattern, message.text)):
                    await message.reply_text(f"{dn} <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a> ᴛᴇxᴛ ᴛᴇʀᴅᴇᴛᴇᴄᴛ ᴅɪ ᴅᴀʟᴀᴍ ʙʟᴀᴄᴋʟɪꜱᴛ")
                    await asyncio.sleep(5)
                    await message.delete()
                    return await message.delete()
    except Exception:
        pass
