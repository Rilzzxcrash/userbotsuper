import requests
from PyroUbot import *

__MODULE__ = "ɢᴇᴍᴘᴀ"
__HELP__ = """

<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴇᴍᴘᴀ</b>

<b>ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}gempa</code>
<i>ᴘᴇɴᴊᴇʟᴀsᴀɴ :</b> ᴄᴇᴋ ɪɴғᴏ sᴇᴋɪᴛᴀʀ ɢᴇᴍᴘᴀ ʙᴍᴋɢ</i></blockquote> """

def get_gempa():
    url = "https://api.botcahx.eu.org/api/search/gempa?apikey=jembot"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") and data.get("result"):
            result = data["result"]["result"]
            return f" ɪɴғᴏ ɢᴇᴍᴘᴀ ᴛᴇʀᴋɪɴɪ\n\n" \
                   f" ᴛᴀɴɢɢᴀʟ: {result['tanggal']}\n" \
                   f" ᴡᴀᴋᴛᴜ: {result['jam']}\n" \
                   f" ʟɪɴᴛᴀɴɢ: {result['Lintang']}\n" \
                   f" ʙᴜᴊᴜʀ: {result['Bujur']}\n" \
                   f" ᴍᴀɢɴɪᴛᴜᴅᴏ: {result['Magnitudo']}\n" \
                   f" ᴋᴇᴅᴀʟᴀᴍᴀɴ: {result['Kedalaman']}\n" \
                   f" ᴘᴏᴛᴇɴsɪ: {result['Potensi']}\n" \
                   f" ᴡɪʟᴀʏᴀʜ: {result['Wilayah']}\n" \
                   f" {result['image']}"
    return "eror."

@PY.UBOT("gempa")
async def gempa_handler(client, message):
    info_gempa = get_gempa()
    await message.reply_text(info_gempa, disable_web_page_preview=False)
