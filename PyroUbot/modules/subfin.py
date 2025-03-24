import re
import aiohttp
from PyroUbot import *
from pyrogram.types import Message

__MODULE__ = "sᴜʙғɪɴᴅᴇʀ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜʙғɪɴᴅᴇʀ

 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}subfin</code>
 ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴜɴᴛᴜᴋ ᴄᴇᴋ sᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ ᴅᴏᴍᴀɪɴ ᴜᴛᴀᴍᴀ</b></blockquote>
"""

async def get_subdomains(domain):
    """Mengambil daftar subdomain dari API."""
    params = {"query": domain, "apikey": API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("status") and "result" in data:
                    return data["result"]
    return None

@PY.UBOT("subfin")
@PY.TOP_CMD
async def subfinder(client, message):
    command_parts = message.text.split(maxsplit=1)

    if len(command_parts) < 2:
        await message.reply("contoh: .subfin contoh.com")
        return

    domain = command_parts[1].strip()

    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        await message.reply("domain tidak valid.")
        return

    processing_msg = await message.reply(f"`proses mencari subdomain dari {domain}...`")

    subdomains = await get_subdomains(domain)

    await processing_msg.delete()  

    if subdomains:
        result_text = f"**subdomain {domain}:**\n\n"
        result_text += "\n".join(f"- `{sub}`" for sub in subdomains)
        await message.reply(result_text)
    else:
        await message.reply("gagal mencari subdomain.")

API_KEY = "jembot" 
API_URL = "https://api.botcahx.eu.org/api/tools/subdomain-finder"
