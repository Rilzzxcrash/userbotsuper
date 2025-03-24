import aiohttp
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from PyroUbot import *


__MODULE__ = "ʜᴇʀᴏ ᴍʟ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴇʀᴏ ᴍʟ ⦫</b>
<blockquote><b>⎆ Perintah :
ᚗ <code>{0}heroml</code> namahero
⊶ Mengambil informasi Hero Mobile Legend.</b></blockquote>
"""

def get_hero_info(hero_name):
    formatted_name = hero_name.replace(" ", "_")
    url = f"https://mobile-legends.fandom.com/wiki/{formatted_name}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1", {"class": "page-header__title"}).text.strip()
    hero_info = soup.find("aside", {"class": "portable-infobox"})
    image_url = hero_info.find("img")["src"] if hero_info.find("img") else None

    details = {}
    for row in hero_info.find_all("div", {"class": "pi-item"}):
        label = row.find("h3")
        value = row.find("div")
        if label and value:
            details[label.text.strip()] = value.text.strip()

    caption = f"<pre>Informasi Hero: {title}\n\n"
    for key, value in details.items():
        caption += f"{key}: {value}\n"
    caption += "</pre>"

    return image_url, caption


@PY.UBOT("heroml")
async def hero_name_handler(client, message):
        hero_name = message.text.split(" ", 1)[-1]
        await message.edit("<pre>Mengambil informasi hero...</pre>")

        try:
            image_url, caption = get_hero_info(hero_name)
            if image_url:
                await message.delete()
                await client.send_photo(message.chat.id, image_url, caption=caption)
            else:
                await message.edit("<pre>Gambar hero tidak ditemukan.</pre>")
        except Exception as e:
            await message.edit(f"<pre>Error: {e}</pre>")
