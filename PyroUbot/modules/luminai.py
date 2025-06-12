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
            "❌ Mohon gunakan format yang benar.\nContoh: <code>.lumin halo</code>"
        )

    prs = await message.reply_text("🔍 Menjawab…")
    text = message.text.split(' ', 1)[1].strip()
    url = f"https://xoo-api.vercel.app/luminai?text={text}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await prs.edit(f"❌ API Error: {resp.status}")
                data = await resp.json()
    except aiohttp.ClientError as e:
        return await prs.edit(f"⚠️ Jaringan gagal: {e}")
    except Exception as e:
        return await prs.edit(f"⚠️ Terjadi kesalahan: {e}")

    # Cek dan ambil respon
    jawaban = None
    if isinstance(data, dict):
        jawaban = data.get("result", {}).get("message") or data.get("message")
        if not jawaban and isinstance(data.get("result"), str):
            jawaban = data["result"]
        if not jawaban and isinstance(data.get("answer"), str):
            jawaban = data["answer"]

    if jawaban:
        await prs.edit(f"<blockquote>{jawaban}</blockquote>")
    else:
        # tampilkan respons lengkap untuk debugging
        await prs.edit(f"❌ Respons API tidak memiliki data yang diharapkan:\n\n```json\n{data}```")
