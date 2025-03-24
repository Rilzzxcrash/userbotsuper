from PyroUbot import *
import requests

__MODULE__ = "ᴄᴏᴜɴᴛʀʏ ɪɴꜰᴏ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴄᴏᴜɴᴛʀʏ ɪɴꜰᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}country</code> [ɴᴀᴍᴀ ɴᴇɢᴀʀᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ɪɴꜰᴏʀᴍᴀꜱɪ ᴛᴇɴᴛᴀɴɢ ꜱᴇꜱᴜᴀᴛᴜ ɴᴇɢᴀʀᴀ.</blockquote>
"""

API_URL = "https://api.siputzx.my.id/api/tools/countryInfo"

@PY.UBOT("country")
async def country_info_cmd(client, message):
    if len(message.command) < 2:
        await message.reply("<i>❌ Harap masukkan nama negara.</i>")
        return

    country_name = message.text.split(None, 1)[1]
    msg = await message.reply("<i>🔍 Mengambil data...</i>")

    try:
        response = requests.get(f"{API_URL}?name={country_name}")
        data = response.json()

        # Debug: Print data untuk melihat struktur respons
        print("Response JSON:", data)

        if response.status_code != 200 or not data.get("status"):
            error_message = data.get("error", "Gagal mengambil data.")
            await msg.edit(f"<b>❌ Gagal mengambil data.</b>\nPesan: {error_message}")
            return

        # Mengambil data dengan pengecekan lebih teliti
        country_data = data.get("data", {})

        country = country_data.get("country", country_name)  # Gunakan input jika kosong
        capital = country_data.get("capital", "Tidak diketahui")
        region = country_data.get("region", "Tidak diketahui")
        population = f"{country_data.get('population', 0):,}" if country_data.get("population") else "Tidak diketahui"
        currency = country_data.get("currency", "Tidak diketahui")
        timezone = country_data.get("timezone", "Tidak diketahui")
        calling_code = f"+{country_data.get('calling_code', 'Tidak diketahui')}"

        # Format hasil
        result_text = f"""
<blockquote>
🌍 <b>Negara:</b> {country}
📍 <b>Ibu Kota:</b> {capital}
🗺️ <b>Wilayah:</b> {region}
👥 <b>Populasi:</b> {population}
💰 <b>Mata Uang:</b> {currency}
🕰️ <b>Zona Waktu:</b> {timezone}
📡 <b>Kode Telepon:</b> {calling_code}
</blockquote>
"""

        await msg.edit(result_text)
    except Exception as e:
        await msg.edit(f"<b>❌ Terjadi kesalahan:</b> {str(e)}")
