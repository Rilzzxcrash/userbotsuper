import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋɢʜ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Stalk GH

Perintah : <code>{0}stalkgh</code> 
    Untuk Stalk Github Menggunakan Username</b></blockquote>
"""

@PY.UBOT("stalkgh")
async def stalkgh(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Please use the command `stalkgh` followed by the github username.")
    
    username = message.command[1]
    chat_id = message.chat.id
    url = f"https://aemt.uk.to/ghstalk?username={username}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and 'user' in data['result'] and len(data['result']['user']) > 0:
                result = data['result']['user']
                photoUrl = f"https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
                caption = f"""
<blockquote><b>Name:</b> <code>{result['name']}</code>
<b>Username:</b> <code>{result['username']}</code>
<b>Followers:</b> <code>{result['followers']}</code>
<b>Following:</b> <code>{result['following']}</code>
<b>Bio:</b> <code>{result['bio']}</code>
<b>ID:</b> <code>{result['idUser']}</code></blockquote>
"""
                photo_path = wget.download(photoUrl)
                await client.send_photo(chat_id, caption=caption, photo=photo_path)
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                
                await jalan.delete()
            else:
                await jalan.edit(f"{ggl} No channel data found.")
        else:
            await jalan.edit(f"{ggl} Failed to retrieve data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
