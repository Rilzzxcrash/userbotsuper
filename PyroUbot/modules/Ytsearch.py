import os
import requests
from PyroUbot import *

# Masukkan API Key Anda di sini
API_KEY = "Fieyzzz"  # Ganti dengan API key yang benar

__MODULE__ = "ʏᴛsᴇᴀʀᴄʜ"
__HELP__ = """
📚 <b>Ytsearch Commands</b>

<blockquote><b>🚦 Perintah : <code>ytsearch</code>
🦠 Penjelasan : Mencari video di YouTube berdasarkan kata kunci.</b></blockquote>
"""

def fetch_youtube(api_url, query):
    """
    Fungsi untuk mengambil hasil pencarian dari API YouTube
    """
    params = {"query": query, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # Memeriksa apakah respons berisi hasil pencarian
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            print("Tidak ada hasil pencarian dalam response:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching YouTube results: {e}")
        return None

async def process_youtube_command(client, message, api_url, command_name):
    """
    Fungsi umum untuk menangani perintah pencarian YouTube
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>Gunakan perintah /{command_name} <kata kunci> untuk mencari video di YouTube.</i></b>")
        return

    query = args[1]
    await message.reply_text("<b><i>🔍 Sedang mencari, mohon tunggu...</i></b>")

    results = fetch_youtube(api_url, query)
    if results:
        # Mengirimkan hasil pencarian sebagai daftar
        response_text = (
            "<b><emoji id=5841235769728962577>📹</emoji> Hasil Pencarian Video di YouTube:</b>\n\n"
        )
        for idx, result in enumerate(results[:5], start=1):  # Menampilkan hingga 5 hasil saja
            title = result.get("title", "Tidak ada judul")
            link = result.get("url", "Tidak ada link")
            duration = result.get("duration", "Tidak diketahui")
            views = result.get("views", "Tidak diketahui")
            response_text += (
                f"<b><emoji id=5841243255856960314>{idx}.</emoji> {title}</b>\n"
                f"<b><emoji id=5843952899184398024>⏱️</emoji> Durasi:</b> {duration}\n"
                f"<b><emoji id=5841243255856960314>👁‍🗨</emoji> Views:</b> {views}\n"
                f"<b><emoji id=5841235769728962577>🔗</emoji> Link:</b> <a href='{link}'>Tonton Video</a>\n\n"
            )
        await message.reply_text(response_text, disable_web_page_preview=True)
    else:
        await message.reply_text("Gagal mencari video. Coba lagi nanti.")

# Handler untuk perintah ytsearch
@PY.UBOT("ytsearch")
async def youtube_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/search/yts"
    await process_youtube_command(client, message, api_url, "ytsearch")
