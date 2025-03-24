import os
import bs4
import wget
import requests
import traceback
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "pinterest"
__HELP__ = """
<blockquote><b>Bantuan Untuk Pinterest</b>

<b>Perintah</b> : <code>{0}pint</code> <b>[link nya]</b>
<b>Penjelasan : Download Foto Pinterest</b>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pinsearch</code> 
   <i>penjelasan:</b> mendowload media dari pencarian.</i></blockquote>

"""

class PinterestMediaDownloader:
	info_url = "https://api.pinterest.com/v3/pidgets/pins/info/?pin_ids={}"
	
	def __init__(self, pin_url):
		self.session = requests.Session()
		self.pin_url = pin_url
		self.pin_id = None
		self.media = []
		self.data = None
		self.best_sizes = []

	def get_pin_id(self):
		history = self.session.get(self.pin_url).history
		self.pin_id = history[-1].headers["location"].split("/")[4] if history else self.pin_url.split("/")[4]

	def get_pin_data(self):
		self.data = self.session.get(self.__class__.info_url.format(self.pin_id)).json()["data"][0]
	  
	def get_pin_media(self): 
		if spd := self.data.get("story_pin_data"):
			for page in spd["pages"]:
				if v := page["blocks"][0].get("video"):
					self.media.append(v.get("video_list")) 

				elif i := page["blocks"][0].get("image"):
					self.media.append(i.get("images"))
				else:
					pass
		elif v := self.data.get("videos"):
			self.media.append(v.get("video_list"))
		elif i := self.data.get("images"):
			self.media.append(i)
		else:
			pass
		
	def get_best_sizes(self):
		for i, m in enumerate(self.media):
			for s in list(m):
				if m[s]["url"].strip().endswith(".m3u8"):
					m.pop(s)
			new_m = sorted(m.values(), key=lambda s: s["width"]*s["height"], reverse=True)
			
			self.best_sizes.append(new_m[0])
			
#pinterest downloader
@PY.UBOT("pint")
async def pinterest(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Untuk mendapatkan media Pinterest lakukan /pints [URL Pinterest]")

    content = message.text.split(None, 1)[1]
    pinterest_downloader = PinterestMediaDownloader(content)
    
    i = await message.reply_text("🔍 <b>Memprosess...</b>")
    
    try:
        pinterest_downloader.get_pin_id()
        pinterest_downloader.get_pin_data()
        pinterest_downloader.get_pin_media()
        pinterest_downloader.get_best_sizes()

        best_media_url = pinterest_downloader.best_sizes[0]["url"]
        file_extension = best_media_url.split('.')[-1]
        caption = f"•\n\nFile type: {file_extension.capitalize()}"
        
        if any('.mp4' in best_media_url for media in pinterest_downloader.best_sizes):
            await message.reply_video(best_media_url, caption=caption)
        elif any('.gif' in best_media_url for media in pinterest_downloader.best_sizes):
            await message.reply_animation(best_media_url, caption=caption)
        else:
            await message.reply_photo(best_media_url, caption=caption)
        
        await i.delete()
    except Exception as err:
        return await i.edit("Maaf, saya tidak dapat mendapatkan informasi tentang file ini.\nCoba lagi nanti atau kirim tautan lain.", disable_web_page_preview=True)

@PY.UBOT("pinsearch")
async def pin(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Example .pinsearch asuna")
    
    a = message.text.split(' ', 1)[1]
    chat_id = message.chat.id
    url = f"https://widipe.com/pinterest?query={a}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            random_result = random.choice(hasil)
            caption = f"""
<emoji id=5841235769728962577>⭐</emoji>Berikut Foto Yang Kamu Minta.

<b>-- 👾 USERBOT 👾 --</b>
"""
            photo_path = wget.download(random_result)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")