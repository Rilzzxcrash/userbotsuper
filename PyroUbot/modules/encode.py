import os
import subprocess
from pyrogram import Client, filters
from PyroUbot import PY
import shutil
from pyrogram.types import Message

__MODULE__ = "ᴇɴᴄʀʏᴘᴛ ʜᴀʀᴅ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Encrypt JS</b>

Perintah:
<code>{0}enc</code> → Balas file .js untuk dienkripsi.

Sumber: Menggunakan JsConfuser untuk obfuscate JavaScript dengan gaya Unicode.</blockquote></b>
"""

# Periksa apakah Node.js sudah terinstal
if not shutil.which("node"):
    raise Exception("⚠️ Node.js belum terinstal. Install dengan `pkg install nodejs` atau sesuai sistem kamu.")

# Isi confuser.js sebagai string
CONFUSER_JS_CODE = """
const fs = require("fs");
const JsConfuser = require("js-confuser");

(async () => {
  const inputFile = process.argv[2];
  const outputFile = process.argv[3];

  const code = fs.readFileSync(inputFile, "utf-8");

  const obfuscatedCode = await JsConfuser.obfuscate(code, {
    target: "node",
            target: "browser",
            hexadecimalNumbers: false,
            controlFlowFlattening: 0.4,
            deadCode: 0.5,
            dispatcher: true,
            identifierGenerator: function () {
                        return "$var$const$" + Math.random().toString(36).substring(7);
            },
            duplicateLiteralsRemoval: true,
            flatten: true,
            globalConcealing: 0.9,
            minify: true,
            movedDeclarations: true,
            objectExtraction: true,
            opaquePredicates: true,
            renameVariables: true,
            renameGlobals: true,
            shuffle: {
        hash: false,
        true: false
            },
            stack: true,
            stringCompression: true,
            stringConcealing: true,
            stringEncoding: 0,
            stringSplitting: false
        });

  const header = `
/*
~ Kode di-obfuscate Hard Obf
~ Telegram: t.me/rugibanget
~ Covz Confuser Unicode Type

© Cella

🔐 Owner : Cella

📘 Obf Version : 3.1

🔩 Type : JS

📆 Date : ${new Date().toISOString().split('T')[0]}

⚔️ Support : NodeJS, Termux

❄ Node Module : 3
*/
`;

const finalCode = `${header}\n${obfuscatedCode};`;

  fs.writeFileSync(outputFile, finalCode, "utf-8");
})();
"""

@PY.UBOT("enc")
@PY.TOP_CMD
async def encrypt_js(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply("😠 Silakan balas file .js untuk dienkripsi.")

    file_info = message.reply_to_message.document
    file_name = file_info.file_name

    if not file_name.endswith('.js'):
        return await message.reply("❌ File harus berekstensi .js!")

    msg = await message.reply("⚡ Mengunduh file...")
    input_path = await client.download_media(message.reply_to_message.document)
    output_path = f"./encrypted_{file_name}"
    temp_confuser = "./confuser_temp.js"

    await msg.edit("⚡ Melakukan hard obfuscation dengan JsConfuser...")

    try:
        # Buat file confuser sementara
        with open(temp_confuser, "w", encoding="utf-8") as f:
            f.write(CONFUSER_JS_CODE)

        result = subprocess.run(
            ["node", temp_confuser, input_path, output_path],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            await msg.edit(f"❌ Gagal melakukan hard encrypt:\n\n{result.stderr}")
            return

        await message.reply_document(
            output_path,
            caption="✅ **File berhasil di-obfuscate!**\n🔒 Menggunakan JsConfuser Unicode"
        )

    except Exception as e:
        await msg.edit(f"❌ Terjadi kesalahan: {e}")

    finally:
        # Cleanup semua file
        if os.path.exists(temp_confuser):
            os.remove(temp_confuser)
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
