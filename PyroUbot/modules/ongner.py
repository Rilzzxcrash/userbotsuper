from PyroUbot import *
import os
import json
import asyncio
import psutil
import random
import requests
import re
import platform
import subprocess
import sys
import traceback
import aiohttp
import filetype
import wget
import math

from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from pyrogram.enums import UserStatus
from PyroUbot import *
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import get_event_loop
from functools import partial
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.types.calls import Call
from pyrogram.errors import ChatAdminRequired, UserBannedInChannel
from pytgcalls.exceptions import NotInCallError
from youtubesearchpython import VideosSearch
from datetime import timedelta
from time import time
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from datetime import datetime
from gc import get_objects
from time import time
from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from bs4 import BeautifulSoup
from io import BytesIO
from pyrogram.errors.exceptions import *
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from httpx import AsyncClient, Timeout
from PyroUbot import *

__MODULE__ = "ᴏɴɢɴᴇʀ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Ongner</blockquote></b>

<blockquote><b>perintah : <code>{0}cping</code> - <code>{0}caddbl</code> - <code>{0}climit</code> - <code>calive</code></blockquote></b>

<blockquote><b>perintah : <code>{0}moire gantenk ga</code> - <code>{0}tes on</code></blockquote></b>

<blockquote><b>- <code>{0}p</code>\n- <code>{0}ok</code>\n- <code>{0}sip</code>\n- <code>{0}love</code>\n- <code>{0}haha</code>\n- <code>{0}kuda</code></blockquote></b>
"""

@PY.INDRI("cping")
async def _(client, message):
    try:
        start = datetime.now()
        await client.invoke(Ping(ping_id=0))
        end = datetime.now()
        uptime = await get_time((time() - start_time))
        delta_ping_formatted = round((end - start).microseconds / 10000, 2)
        pong = await EMO.PING(client)
        tion = await EMO.MENTION(client)
        yubot = await EMO.UBOT(client)
        babi = client.me.is_premium
        if babi:
            _ping = f"""
<blockquote>{pong} ᴘᴏɴɢ : {str(delta_ping_formatted).replace('.', ',')} ms
{tion} ᴜsᴇʀʙᴏᴛ ᴏɴ ʙᴀɴɢ mor</blockquote>

<blockquote><b>-- 👾 USERBOT PREMIUM 👾 --</b></blockquote>
"""
            await message.reply(_ping)
        else:
            await message.reply(f"<blockquote>ᴘᴏɴɢ : {str(delta_ping_formatted).replace('.', ',')} ms\nᴜsᴇʀʙᴏᴛ ᴏɴ ʙᴀɴɢ mor</blockquote>\n\n<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>")
    except Exception as r:
        print(r)

@PY.INDRI("caddbl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}proceꜱꜱing..."

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id in blacklist:
            txt = f"""
<blockquote><b>{grp} ɢʀᴏᴜᴘ: {message.chat.title}</blockquote></b>\n<blockquote><b>{ktrn} ᴋᴇᴛ: sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ ᴊᴇᴍʙᴏᴛ</blockquote></b>

<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""
        else:
            await add_to_vars(client.me.id, "BL_ID", chat_id)
            txt = f"""
<blockquote><b>{grp} ɢʀᴏᴜᴘ: {message.chat.title}</blockquote></b>\n<blockquote><b>{ktrn} ᴋᴇᴛ: ʙᴇʀʜᴀsɪʟ ᴅɪ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀʟᴀᴍ ʟɪsᴛ ᴊᴇᴍʙᴏᴛ</blockquote></b>

<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))

@PY.INDRI("climit")
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"{prs}processing . . .")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1) 
    if status and hasattr(status, "text"):
        pjg = len(status.text)
        print(pjg)
        if pjg <= 100:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ</b>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ</b>
<b>{yubot} ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>sᴛᴀᴛᴜs ᴀᴋᴜɴ  : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʏᴀ</b>
<b>ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ</b>
<b>ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ</b>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ</b> 
<b>{yubot} ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>sᴛᴀᴛᴜs ᴀᴋᴜɴ  : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʏᴀ</b>
<b>ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ</b>
<b>ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>

<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    else:
        print("Status tidak valid atau status.text tidak ada")

@PY.INDRI("cgikes")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    
    _msg = f"{prs}proceꜱꜱing..."
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)
    
    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"{ggl}{message.text.split()[0]} type [reply]")

    if not message.reply_to_message:
        return await gcs.edit(f"{ggl}{message.text.split()[0]} type [reply]")

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    _gcs = f"""
<blockquote><b>{bcs}ʙʀᴏᴀᴅᴄᴀsᴛ ғᴏʀᴡᴀʀᴅ ᴅᴏɴᴇ</blockquote></b>
<blockquote><b>{brhsl} sᴜᴄᴄᴇs {done} ɢʀᴏᴜᴘ</b>
<b>{ggl} ғᴀɪʟᴇᴅ {failed} ɢʀᴏᴜᴘ</blockquote></b>

<blockquote><b>-- 👾 USERBOT PREMIUM 👾 --</b></blockquote>
"""
    return await message.reply(_gcs)


@PY.INDRI("calive")
async def _(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
    except Exception as error:
        await message.reply(error)

@PY.INDRI("calive")
async def _(client, inline_query):
    psr = await EMO.PASIR(client)
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            try:
                peer = my._get_my_peer[my.me.id]
                users = len(peer["pm"])
                group = len(peer["gc"])
            except Exception:
                users = random.randrange(await my.get_dialogs_count())
                group = random.randrange(await my.get_dialogs_count())
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y") if get_exp else "None"
            if my.me.id in await get_list_from_vars(client.me.id, "ULTRA_PREM"):
                status = "SuperUltra"
            else:
                status = "Premium"
            button = BTN.ALIVE(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            psr = await EMO.PASIR(client)
            msg = f"""
<blockquote>{bot.me.mention}
    status: {status} 
       {psr} expired_on: {exp} 
            dc_id: {my.me.dc_id}
            ping_dc: {ping} ms
            peer_users: {users} users
            peer_group: {group} group
            start_uptime: {uptime}</blockquote> 
<blockquote><b>👾 USERBOT PREMIUM 👾</b></blockquote>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=300,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )

@PY.INDRI("cinpit")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    mg = await message.reply(f"{prs}menambahkan pengguna!")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            f"{ktrng}beri saya pengguna untuk ditambahkan!\nperiksa menu bantuan untuk info lebih lanjut!"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"{brhsl}berhasil ditambahkan {len(user_list)} ke grup ini")

@PY.INDRI("cautobc")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    bcs = await EMO.BROADCAST(client)
    mng = await EMO.MENUNGGU(client)
    ggl = await EMO.GAGAL(client)   
    msg = await message.reply(f"{prs}proceꜱꜱing...")
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit(
                f"{ggl}harap ꜱetting text terlebih dahulu"
            )

        if client.me.id not in AG:
            await msg.edit(f"{brhsl}auto gcaꜱt di aktifkan")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_list_from_vars(client.me.id, "BL_ID")
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                    ):
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(f"""
{bcs}auto_gcaꜱt done
putaran {done}
{brhsl}ꜱucceꜱ {group} group
{mng}wait {delay} minuteꜱ
""",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit(f"{brhsl}auto gcast dinonaktifkan")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit(
                f"{ggl}{message.text.split()[0]} text - [value]"
            )
        await add_auto_text(client, value)
        return await msg.edit(f"{brhsl}berhasil di simpan")

    elif type == "delay":
        if not int(value):
            return await msg.edit(
                f"{ggl}{message.text.split()[0]} delay - [value]"
            )
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"{brhsl}barhasil ke setting {value} menit"
        )

    elif type == "remove":
        if not value:
            return await msg.edit(
                f"{ggl}{message.text.split()[0]} remove - [value]"
            )
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit(f"{brhsl}semua text berhasil dihapus")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"{brhsl}text ke {value+1} berhasil dihapus"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit(f"{ggl}auto gcast text kosong")
        txt = "daftar auto gcast text\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}> {x}\n\n"
        txt += f"\nuntuk menghapus text:\n{message.text.split()[0]} remove [angka/all]"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit(f"{brhsl}auto cek limit dinonaktifkan")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit(f"{brhsl}auto cek limit started")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
             return await msg.edit(f"{ggl}{message.text.split()[0]} limit - [value]")

    else:
        return await msg.edit(f"{ggl}{message.text.split()[0]} [query] - [value]")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)

@PY.INDRI("clvc")
async def leave_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    try:
        mex = await message.reply(f"{prs}proccesing...")
        await client.call_py.leave_call(message.chat.id)
        await mex.edit(f"{brhsl}berhasil turun dari obrolan suara")
    except NotInCallError:
        await mex.edit(f"{ggl}belum bergabung ke voice chat")
    except UserBannedInChannel:
        pass
    except Exception as e:
        print(e)

@PY.INDRI("cjvc")
async def join_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    try:
        mex = await message.reply(f"{prs}proccesing...")
        await client.call_py.play(message.chat.id)
        await client.call_py.mute_stream(message.chat.id)
        await mex.edit(f"{brhsl}**berhasil join ke voice chat**")        
    except ChatAdminRequired:
        await mex.edit(f"{ggl}**maaf tidak bisa join vc**")
    except UserBannedInChannel:
        pass
    except Exception as e:
        print(e)
    
@PY.INDRI("pada on ga")
async def padaonga(client, message):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n")
    
@PY.INDRI("moire gantenk ga")
async def moiregantenkga(client, message):
    await message.reply(
       "<blockquote><b>ya benar dia sangat gantenk sekali\n\n- dia baik\n- dia manis\n- dia lucu\n- dia imut\n- dia konbrut awsjshsjhsjs\n\nidaman banget lah pokonya moire nih</blockquote></b>")

@PY.INDRI("tes on")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>on selalu moire gantenk</blockquote></b>")
        
@PY.INDRI("kuda")
async def _(client, message):
    await message.react("🦄")

@PY.INDRI("love")
async def _(client, message):
    await message.react("❤")

@PY.INDRI("sip")
async def _(client, message):
    await message.react("👍")

@PY.INDRI("ok")
async def _(client, message):
    await message.react("👌")

@PY.INDRI("haha")
async def _(client, message):
    await message.react("😹")

@PY.INDRI("p")
async def _(client, message):
    await message.react("👋")

@PY.INDRI("wow")
async def _(client, message):
    await message.react("😨")
