import asyncio
import random

import requests
from pyrogram import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *

from PyroUbot import *

DEFAULTUSER = "Nay"


NOBLE = [
    "╲╲╲┏┓╭╮╱╱╱\n╲╲╲┗┓┏┛┃╭╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏╯╱╱\n╱╱┏┻┳┳┻┫┗┓╱╱╱\n╱╱╰┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗╮╲╲\n╱╱╱╱╰╯╰┛╲╲",
    "┏╮\n┃▔┃▂▂┏┓┏┳┓\n┃▂┣┻╮┃┃▂┃▂┏╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗╮┃▔▔▔┃▔┏╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗╮\n┗┻┻┛",
    "┏┓┏┳┳┳┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗┻┛┗┛┗┛\n­­­­­­­­­YOU",
    "╦╔╗╗╔╔ \n║║║║║╠ \n╚═╚╝╚╝╚ \n╦╦╔╗╦╦   \n╚╦╝║║║║ \n╩╚╝╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\\../') \n╔╝╚╗..( . ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭╱▔▔▔▔╲╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭╮▔▏┊┊▕▔╭╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰╲╱╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­­­­­­­­­­YOU",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳┳╮╭┳╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰┻╯╰╯╰╯",
    "┊┊╭╮┊┊┊┊┊┊┊┊┊┊┊ \n╋╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭┳╮╭┓┊╭╮╭╮ \n╭╋╋╯┣╯┃┊┃╰╋╯ \n╰╯┊╰╯┊╰┛┊╰",
]


__MODULE__ = "ᴀɴɪᴍᴀꜱɪ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴀsɪ ⦫<b>

<blockquote><b>⎆ perintah :
ᚗ <code>{0}dino</code>
ᚗ <code>{0}awk</code>
ᚗ <code>{0}loveyou</code>
ᚗ <code>{0}ange</code>
ᚗ <code>{0}hmm</code>
ᚗ <code>{0}lipkol</code>
ᚗ <code>{0}kntl</code>
ᚗ <code>{0}ajg</code>
ᚗ <code>{0}kocok</code>
ᚗ <code>{0}heli</code>
ᚗ <code>{0}y</code>
ᚗ <code>{0}nakal</code>
ᚗ <code>{0}tank</code>
ᚗ <code>{0}nah</code>
ᚗ <code>{0}tembak</code>
ᚗ <code>{0}piss</code>
ᚗ <code>{0}bundir</code>
ᚗ <code<{0}bot</code>
ᚗ <code>{0}sepongebob</code></b></blockquote>
"""


@PY.UBOT("loveyou")
@PY.TOP_CMD
async def lopeyo(client, message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await message.reply(reply_text)


@PY.UBOT("hmm")
@PY.TOP_CMD
async def hmmm(client, message):
    mg = await message.reply(
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱╱▔▔▔▔▔╲╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰▏▊▕▕▋▕▕╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )


@PY.UBOT("ktl")
@PY.TOP_CMD
async def kntl(client, message):
    emoji = get_text(message)
    kontol = MEMES.GAMBAR_KONTOL
    if emoji:
        kontol = kontol.replace("⡀", emoji)
    await message.reply(kontol)


@PY.UBOT("penis")
@PY.TOP_CMD
async def pns(client, message):
    emoji = get_text(message)
    titid = MEMES.GAMBAR_TITIT
    if emoji:
        titid = titid.replace("😋", emoji)
    await message.reply(titid)


@PY.UBOT("heli")
@PY.TOP_CMD
async def helikopter(client, message):
    await message.reply(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


@PY.UBOT("tembak")
@PY.TOP_CMD
async def dornembak(client, message):
    await message.reply(
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤ ҉\n" r"_/﹋\_" "\nMau Jadi Pacarku Gak?!",
    )


@PY.UBOT("bundir")
@PY.TOP_CMD
async def ngebundir(client, message):
    await message.reply(
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@PY.UBOT("awk")
@PY.TOP_CMD
async def awikwok(client, message):
    await message.reply(
        "██▀▀▀██\n"
        "▄▀█▄▄▄▄▀█▄▄▄\n"
        "▄▀█▄▄██▄▄\n"
        "▄▄▄▀▀▄▄▄▄▀▀▄\n"
        "▀▀▀▀▀▀\n`Awkwokwokwok..`",
    )


@PY.UBOT("ya")
@PY.TOP_CMD
async def ysaja(client, message):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )
@PY.UBOT("bot")
@PY.TOP_CMD
async def bot(client, message):
    await message.reply(
       "╔╗╔╦══╦═╦═╦══╦═╦══╗\n"
       "║║║║══╣╦╣╬║╔╗║║╠╗╔╝\n"
       "║╚╝╠══║╩╣╗╣╔╗║║║║║\n"
       "╚══╩══╩═╩╩╩══╩═╝╚╝\n", 
    ) 


@PY.UBOT("tank")
async def tank(client, message):
    await message.reply(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


@PY.UBOT("babi")
@PY.TOP_CMD
async def babi(client, message):
    await message.reply(
        "┈┈┏╮╭┓┈╭╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰╯\n"
        "┈╭┻╮╲┗╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣╯┈\n"
        "┈╰┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@PY.UBOT("ange")
@PY.TOP_CMD
async def piciieess(client, message):
    e = await message.edit("Ayanggg 😖")
    await asyncio.sleep(2)
    await e.edit("Aku Ange 😫")
    await asyncio.sleep(2)
    await e.edit("Ayuukk Picies Yang 🤤")


@PY.UBOT("lipkol")
@PY.TOP_CMD
async def lipkoll(client, message):
    e = await message.edit("Ayanggg 😖")
    await asyncio.sleep(2)
    await e.edit("Kangeeen 👉👈")
    await asyncio.sleep(2)
    await e.edit("Pingiinn Slipkool Yaaang 🥺👉👈")


@PY.UBOT("nakal")
@PY.TOP_CMD
async def nakall(client, message):
    e = await message.edit("Ayanggg ih🥺")
    await asyncio.sleep(2)
    await e.edit("Nakal Banget Dah Ayang 🥺")
    await asyncio.sleep(2)
    await e.edit("Aku Gak Like Ayang 😠")
    await asyncio.sleep(2)
    await e.edit("Pokoknya Aku Gak Like Ih 😠")


@PY.UBOT("piss")
@PY.TOP_CMD
async def peace(client: Client, message: Message):
    await message.reply(
        "┈┈┈┈PEACE MAN┈┈┈┈\n"
        "┈┈┈┈┈┈╭╮╭╮┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┗┛┣┳╮┈┈┈┈\n"
        "┈┈┈┈┈╭┻┓┃┃┈┈┈┈\n"
        "┈┈┈┈┈┃╲┏╯┻┫┈┈┈┈\n"
        "┈┈┈┈┈╰╮╯┊┊╭╯┈┈┈┈\n",
    )


@PY.UBOT("spongebob")
@PY.TOP_CMD
async def spongebobss(client: Client, message: Message):
    await message.reply(
        "╲┏┳┓╲╲\n"
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲\n"
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲\n"
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲\n"
        "╲┃◯┃╭╮╰╯┏┳╯╲\n"
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲\n"
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲\n",
    )



@PY.UBOT("kocok")
@PY.TOP_CMD
async def kocokk(client, message):
    e = await message.edit("KOCOKINNNN DONG SAYANKKKKK🤤🤤🥵🥵")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊====D💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT**")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT AAAHHH BASAHH.....**")
    await asyncio.sleep(0.2)
    await e.edit("**AHHH ENAKKKKK SAYANGGGG🤤🤤🥵🥵**")


@PY.UBOT("dino")
@PY.TOP_CMD
async def adadino(client: Client, message: Message):
    typew = await message.edit("`DIN DINNN.....`")
    await asyncio.sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    await asyncio.sleep(1)
    await typew.edit("`🧎🦖`")
    await asyncio.sleep(2)
    await typew.edit("`-TAMAT-`")


@PY.UBOT("ajg")
@PY.TOP_CMD
async def anjg(client, message):
    await message.reply(
        "╥╭╮┳\n"
        "╢╭╮╭┫┃▋▋▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰┫┈┈┈┈┈╰╯╰┳╯┣\n"
        "╢┊┊┃┏┳┳┓┏┳┫┊┊┣\n"
        "╨┗┛┗┛┗┛┗┛┻\n",
    )


@PY.UBOT("nah")
@PY.TOP_CMD
async def nahlove(client, message):
    typew = await message.reply("`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *Ini Buat Kamu`")
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  *Tapi Bo'ong`")




