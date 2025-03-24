import asyncio
from time import sleep
from PyroUbot import *

__MODULE__ = "toxic"
__HELP__ = """
 <blockquote><b>Bantuan Untuk toxic</b>

• <b>Perintah</b> : <code>{0}jamet</code>
• <b>Penjelasan : gatau gabut doang.</b>

• <b>Perintah</b> : <code>{0}vir</code>
• <b>Penjelasan : gatau gabut doang.</b>

• <b>Perintah</b> : <code>{0}ppx</code>
• <b>Penjelasan : gatau gabut doang.</b>

• <b>Perintah</b> : <code>{0}kiss</code>
• <b>Penjelasan : gatau gabut doang.</b>

• <b>Perintah</b> : <code>{0}pc</code>
• <b>Penjelasan : gatau gabut doang.</b>

• <b>Perintah</b> : <code>{0}hah</code>
• <b>Penjelasan : gatau gabut doang.</b>

• <b>Perintah</b> : <code>{0}gembel</code>
• <b>Penjelasan : gatau gabut doang.</b></blockquote>

"""

@PY.UBOT("jamet")
async def bulan(client, message):
    animation_interval = 0.2
    animation_ttl = range(96)
    await message.edit("WOII..")
    animation_chars = [
        "Lu yang rusuh sanah sinih?",
        "Ni gw bilangin ya",
        "GAUSAH SO ASIK",
        "EMANG LU TERKENAL?",
        "Cuma kacung di real sok mau rusuh",
        "Orang yang kaya lu ni harus gw katain",
        "Jangan sok tinggi di telegram bgstt",
        "BOCAH KAMPUNG",
        "THOLOL KALAU LU MAU RUSUH JANGAN DISINI THOLOL",
        "Mending lu bantu mak lu sono, dari pada ga ada kerjaan",]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 32])


@PY.UBOT("vir")
async def izzyganteng(client, message):
    e = await message.edit("OOOO")
    await e.edit("INI YANG VIRTUAL")
    await e.edit("YANG KATANYA SAYANG BANGET")
    await e.edit("TAPI TETEP AJA DI TINGGAL")
    await e.edit("NI INGET")
    await e.edit("TANGANNYA AJA GA BISA DI PEGANG")
    await e.edit("APALAGI KEMALUAN NYA")
    await e.edit("BHAHAHAHA")
    await e.edit("KASIAN BAHAHAHA GBLOK MKN TUH VIRTUAL")


@PY.UBOT("ppx")
async def izzygantengbgt(client, message):
    typew = await message.edit("`OI PPKK LU KALAU MAU NIMBRUNG, NIMBRUNG AJA GOBLOKKK JGN RUSUHH DISINII THOLOL!!`")


@PY.UBOT("kiss")
async def izzyemangganteng(client, message):
    e = await message.edit("`CUIHHHH, NIH GW CIUM PALA OTAK KAU, KAU PUNYA OTAK GA GBLKK!!`")


@PY.UBOT("pc")
async def izzypalingganteng(client, message):
    typew = await message.edit("`Apa kau pantex, mau apa mau pc pc gw anying`")


# Create by myself @Boysz


@PY.UBOT("hah")
async def izzygantengsekali(client, message):
    await message.edit( "`EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK!!`")


@PY.UBOT("gembel")
async def izzyemangpalingganteng(client, message):
    animation_chars = [
            "`MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!`",
    ]
    animation_interval = 2
    animation_ttl = range(11)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 11])
