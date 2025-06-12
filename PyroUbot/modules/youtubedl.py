from PyroUbot import *
import asyncio
import os
from datetime import timedelta
from time import time
import aiohttp

from pyrogram.errors import FloodWait, MessageNotModified

__MODULE__ = "ʏᴏᴜᴛᴜʙᴇ"
__HELP__ = """
📚 <b>--Folder Untuk Youtube--</b>

<blockquote><b>🚦 Perintah : <code>{0}song</code>
🦠 Penjelasan : Mendownload Music Yang Di Inginkan.</b></blockquote>
<blockquote><b>🚦 Perintah : <code>{0}vsong</code>
🦠 Penjelasan : Mendownload Video Yang Di Inginkan.</b></blockquote>
"""

APIKEY = "free"  # <-- Ganti dengan apikey dari SimpleBot

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "kb", 2: "mb", 3: "gb", 4: "tb"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)} hari, " if days else "")
        + (f"{str(hours)} jam, " if hours else "")
        + (f"{str(minutes)} menit, " if minutes else "")
        + (f"{str(seconds)} detik, " if seconds else "")
        + (f"{str(milliseconds)} mikrodetik, " if milliseconds else "")
    )
    return tmp[:-2]


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("" for _ in range(int(percentage // 10))),
            "".join("~" for _ in range(10 - int(percentage // 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nestimasi: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        try:
            await message.edit(f"{type_of_ps}\n{tmp}")
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except MessageNotModified:
            pass


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


@PY.UBOT("song")
@PY.TOP_CMD
async def song_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply_text(f"{ggl} audio tidak ditemukan ! mohon masukan judul video dengan benar.")

    query = message.text.split(None, 1)[1]
    infomsg = await message.reply_text(f"{prs} pencarian...")

    search_url = f"https://api-simplebot.vercel.app/search/youtube?apikey={APIKEY}&q={query}"
    try:
        result = await fetch_json(search_url)
        video = result["result"][0]
        video_url = video["url"]
    except Exception as e:
        return await infomsg.edit(f"{ggl} Gagal mencari lagu!\n\n{e}")

    download_url = f"https://api-simplebot.vercel.app/download/ytmp3?apikey={APIKEY}&url={video_url}"
    try:
        audio = await fetch_json(download_url)
        if "result" not in audio:
            return await infomsg.edit(f"{ggl} Gagal mendownload audio!\n\nTidak ada data `result`.\n\n{audio}")

        result = audio["result"]

        title = result.get("title")
        audio_url = result.get("media") or result.get("url")
        duration = result.get("duration") or result.get("metadata", {}).get("lengthSeconds", "Tidak diketahui")
        channel = result.get("uploader") or result.get("author", {}).get("name", "Tidak diketahui")
        thumb = result.get("thumbnail") or result.get("metadata", {}).get("thumbnail")
        video_url = result.get("url") or video_url  # fallback ke video sebelumnya jika hilang

        if not all([title, audio_url, channel, thumb]):
            return await infomsg.edit(
                f"{ggl} Gagal mendownload audio!\n\nBeberapa data penting hilang.\n\n{result}"
            )

    except Exception as e:
        return await infomsg.edit(f"{ggl} Gagal mendownload audio!\n\n{e}")

    audio_path = f"{title}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(audio_url) as resp:
            with open(audio_path, "wb") as f:
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

    await client.send_audio(
        chat_id=message.chat.id,
        audio=audio_path,
        caption=f"🎵 <b>{title}</b>\n🕒 {duration}\n📺 {channel}\n🔗 <a href='{video_url}'>Link Video</a>",
        performer=channel,
        title=title,
        thumb=thumb,
        reply_to_message_id=message.id,
    )

    await infomsg.delete()
    if os.path.exists(audio_path):
        os.remove(audio_path)


@PY.UBOT("vsong")
@PY.TOP_CMD
async def vsong_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply_text(f"{ggl} video tidak ditemukan ! mohon masukan judul video dengan benar.")

    query = message.text.split(None, 1)[1]
    infomsg = await message.reply_text(f"{prs} pencarian...")

    search_url = f"https://api-simplebot.vercel.app/search/youtube?apikey={APIKEY}&q={query}"
    try:
        result = await fetch_json(search_url)
        video = result["result"][0]
        video_url = video["url"]
    except Exception as e:
        return await infomsg.edit(f"{ggl} Gagal mencari video!\n\n{e}")

    download_url = f"https://api-simplebot.vercel.app/download/ytmp4?apikey={APIKEY}&url={video_url}"
    try:
        vid = await fetch_json(download_url)
        video_url_direct = vid["result"]["url"]
        title = vid["result"]["title"]
        duration = vid["result"]["duration"]
        channel = vid["result"]["uploader"]
        thumb = vid["result"]["thumbnail"]
    except Exception as e:
        return await infomsg.edit(f"{ggl} Gagal mendownload video!\n\n{e}")

    video_path = f"{title}.mp4"
    async with aiohttp.ClientSession() as session:
        async with session.get(video_url_direct) as resp:
            with open(video_path, "wb") as f:
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

    await client.send_video(
        chat_id=message.chat.id,
        video=video_path,
        caption=f"🎬 <b>{title}</b>\n🕒 {duration}\n📺 {channel}\n🔗 <a href='{video_url}'>Link Video</a>",
        supports_streaming=True,
        reply_to_message_id=message.id,
    )

    await infomsg.delete()
    if os.path.exists(video_path):
        os.remove(video_path)
