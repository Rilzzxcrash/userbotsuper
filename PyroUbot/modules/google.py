import aiohttp
from PyroUbot import *

__MODULE__ = "ɢᴏᴏɢʟᴇ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Google

perintah : <code>{0}google [query]</code>
    search google</b></blockquote>
"""

@PY.UBOT("gg|google|googlesearch")
async def google_search(client, message):
    webevent = await message.reply("ᴍᴇɴᴇʟᴜsᴜʀɪ ɢᴏᴏɢʟᴇ...")
    match = get_arg(message)
    if not match:
        return await webevent.edit(f"{message.text} ǫᴜᴇʀʏ")
    
    search_query = match.strip()
    api_url = f"https://aemt.uk.to/googlesearch?query={search_query}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                gresults = await response.json()
                msg = ""
                for result in gresults.get("result", []):
                    try:
                        title = result.get("title")
                        link = result.get("link")
                        desc = result.get("description")
                        msg += f"<b>- {title}</b>\n[𝗟𝗶𝗻𝗸 𝗦𝗼𝘂𝗿𝗰𝗲]({link})\n<blockquote><b>{desc}</b></blockquote>"
                    except Exception as e:
                        print(f"Error processing result: {e}")
                
                return await webevent.edit(
                    "\n\nʀᴇsᴜʟᴛs:\n"
                    f"{msg}",
                    disable_web_page_preview=True,
                )
            else:
                return await webevent.edit("ᴇʀʀᴏʀ: ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀᴘɪ")
