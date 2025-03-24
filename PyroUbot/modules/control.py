from PyroUbot import *

__MODULE__ = "ᴄᴏɴᴛʀᴏʟ"
__HELP__ = """
<blockquote>Bantuan Untuk Control

perintah : <code>{0}prefix</code>
   untuk merubah prefix/handler perintah

perintah : <code>{0}creat</code>
   untuk membuat group atau channel

perintah : <code>{0}emoji</code> query emojiprem
   untuk merubah emoji pada tampilan tertentu

query:
    ><code>{0}pong</code>
    ><code>{0}owner</code>
    ><code>{0}ubot</code>
    ><code>{0}gcast</code>
    ><code>{0}sukses</code>
    ><code>{0}gagal</code>
    ><code>{0}proses</code>
    ><code>{0}group</code>
    ><code>{0}catatan</code>
    ><code>{0}afk</code>
    ><code>{0}waktu</code>
    ><code>{0}alasan</code></blockquote>
"""


@PY.UBOT("creat")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"{message.text} [group/channel] [name/titlee]")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("memproꜱeꜱ...")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram grup: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram channel: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )


@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs}memproses...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"{ggl}{message.text} [simbol]")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "no":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(f"<blockquote><b>{brhsl}prefix telah diubah ke: {parsed_prefix}</blockquote></b>\n\n<blockquote><b>ᴀᴡᴀs ᴋᴀʟᴏ ʙᴜᴀᴛ ᴘʀᴇғɪx ᴊᴀɴɢᴀɴ sᴀᴍᴘᴇ ʟᴜᴘᴀ ᴘʀᴇғɪx ʏᴀɴɢ ʟᴜ ɢᴀɴᴛɪ ᴀᴘᴀ !!</blockquote></b>")
        except Exception as error:
            return await Tm.edit(str(error))


@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    msg_afk = (
        f"<blockquote><b>{tion}sedang afk\n{ktrng}alasan: {reason}</blockquote></b>"
        if reason
        else f"{tion}sedang afk"
      )
    await set_vars(client.me.id, "AFK", db_afk)
    return await message.reply(msg_afk)



@PY.NO_CMD_UBOT("AFK", ubot)
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        rpk = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        afk_text = (
            f"<blockquote><b>{tion}sedang afk\n{mng}waktu: {afk_runtime}\n{ktrng}alasan: {afk_reason}</blockquote></b>"
            if afk_reason
            else f"""
<blockquote><b>hello {rpk}
tuan saya sedang afk selama : {afk_runtime}
mohon tunggu beberapa waktu</blockquote></b>
"""
        )
        return await message.reply(afk_text)


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = f"<blockquote><b>{tion}kembali online\n{mng}afk selama: {afk_runtime}</blockquote></b>"
        await message.reply(afk_text)
        return await remove_vars(client.me.id, "AFK")


@PY.UBOT("emoji")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        msg = await message.reply(f"{prs}memproses...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                f"{ggl}beli prem dulu anjg"
            )

        if len(message.command) < 3:
            return await msg.edit(f"{ggl}tolong masukkan query dan valeu nya")

        query_mapping = {
          "pong": "EMOJI_PING",
          "owner": "EMOJI_MENTION",
          "ubot": "EMOJI_USERBOT",
          "proses": "EMOJI_PROSES",
          "gcast": "EMOJI_BROADCAST",
          "sukses": "EMOJI_BERHASIL",
          "gagal": "EMOJI_GAGAL",
          "catatan": "EMOJI_KETERANGAN",
          "group": "EMOJI_GROUP",
          "menunggu": "EMOJI_MENUNGGU",
          "alasan": "EMOJI_ALASAN",
          "waktu": "EMOJI_WAKTU",
          "afk": "EMOJI_AFKA",
        }
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"{brhsl}emoJi berhasil di setting ke: <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit(f"{ggl}tidak dapat menemukan emoji premium")
        else:
            await msg.edit(f"{ggl}mapping tidak ditemukan")

    except Exception as error:
        await msg.edit(str(error))

