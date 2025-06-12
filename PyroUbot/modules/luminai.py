import aiohttp
from PyroUbot import *

__MODULE__ = "luminai"
__HELP__ = """
<blockquote><b>Bantuan Untuk LuminAI

Perintah : <code>{0}lumin</code>
    Dapat mengobrol dengan AI</b></blockquote>
"""

@PY.UBOT("lumin")
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format yang benar.\nContoh: <code>.lumin halo</code>"
        )

    prs = await message.reply_text("<emoji id=5319230516929502602>🔍</emoji> Menjawab...")
    text = message.text.split(' ', 1)[1]

    url = f"https://xoo-api.vercel.app/luminai?text={text}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await prs.edit(f"❌ API Error: {resp.status}")
                data = await resp.json()

        if "result" in data and "message" in data["result"]:
            jawaban = data["result"]["message"]
            await prs.edit(f"<blockquote>{jawaban}</blockquote>")
        else:
            await prs.edit("❌ Respons API tidak memiliki data yang diharapkan.")

    except Exception as e:
        await prs.edit(f"⚠️ Terjadi kesalahan: {e}")
