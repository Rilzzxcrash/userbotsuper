from PyroUbot import *



class EMO:
    async def PING(client):
        emot_1 = await get_vars(client.me.id, "EMOJI_PING")
        emot_ping = emot_1 if emot_1 else "4943170357382087999"
        _pong = f"<emoji id={emot_ping}>😉</emoji>"
        return _pong

    async def MENTION(client):
        emot_2 = await get_vars(client.me.id, "EMOJI_MENTION")
        emot_tion = emot_2 if emot_2 else "5217822164362739968"
        _men = f"<emoji id={emot_tion}>👑</emoji>"
        return _men

    async def UBOT(client):
        emot_3 = await get_vars(client.me.id, "EMOJI_USERBOT")
        emot_xbot = emot_3 if emot_3 else "4943012379895005986"
        _ubt = f"<emoji id={emot_xbot}>😊</emoji>"
        return _ubt
    
    async def PROSES(client):
        emot_4 = await get_vars(client.me.id, "EMOJI_PROSES")
        emot_prs = emot_4 if emot_4 else "5789858554890425372"
        if client.me.is_premium:
            _prses = f"<emoji id={emot_prs}>🤔</emoji>"
        else:
            _prses = ""
        return _prses
    
    async def BERHASIL(client):
        emot_5 = await get_vars(client.me.id, "EMOJI_BERHASIL")
        emot_brhsl = emot_5 if emot_5 else "5206607081334906820"
        if client.me.is_premium:
            _berhasil = f"<emoji id={emot_brhsl}>✔️</emoji>"
        else:
            _berhasil = ""
        return _berhasil

    async def GAGAL(client):
        emot_6 = await get_vars(client.me.id, "EMOJI_GAGAL")
        emot_ggl = emot_6 if emot_6 else "5210952531676504517"
        if client.me.is_premium:
            _gagal = f"<emoji id={emot_ggl}>❌</emoji>"
        else:
            _gagal = ""
        return _gagal

    async def BROADCAST(client):
        emot_7 = await get_vars(client.me.id, "EMOJI_BROADCAST")
        emot_gcs = emot_7 if emot_7 else "5929509352095354418"
        if client.me.is_premium:
            _bc = f"<emoji id={emot_gcs}>🎺</emoji> "
        else:
            _bc = ""
        return _bc

    async def BL_GROUP(client):
        emot_8 = await get_vars(client.me.id, "EMOJI_GROUP")
        emot_gc = emot_8 if emot_8 else "5260341314095947411"
        if client.me.is_premium:
            _grp = f"<emoji id={emot_gc}>👀</emoji>"
        else:
            _grp = ""
        return _grp

    async def BL_KETERANGAN(client):
        emot_9 = await get_vars(client.me.id, "EMOJI_KETERANGAN")
        emot_ktrng = emot_9 if emot_9 else "6208270338971669367"
        if client.me.is_premium:
            _ktrn = f"<emoji id={emot_ktrng}>🗒</emoji>"
        else:
            _ktrn = ""
        return _ktrn     

    async def MENUNGGU(client):
        emot_10 = await get_vars(client.me.id, "EMOJI_MENUNGGU")
        emot_mng = emot_10 if emot_10 else "5413704112220949842"
        if client.me.is_premium:
            _ktr = f"<emoji id={emot_mng}>⏰</emoji>"
        else:
            _ktr = ""
        return _ktr

    async def PUTARAN(client):
        emot_11 = await get_vars(client.me.id, "EMOJI_PUTARAN")
        emot_ptr = emot_11 if emot_11 else "5361600266225326825"
        if client.me.is_premium:
            mmk = f"<emoji id={emot_ptr}>✈️</emoji>"
        else:
            mmk = ""
        return mmk

    async def AEFKA(client):
        emot = await get_vars(client.me.id, "EMOJI_AFKA")
        emot_ji = emot if emot else "5805504652598316759"
        if client.me.is_premium:
            mmk = f"<emoji id={emot_ji}>👣</emoji> "
        else:
            mmk = ""
        return mmk

    async def ALASAN(client):
        emot = await get_vars(client.me.id, "EMOJI_ALASAN")
        emot_ji = emot if emot else "6026321200597176575"
        if client.me.is_premium:
            mmk = f"<emoji id={emot_ji}>🃏</emoji> "
        else:
            mmk = ""
        return mmk

    async def WAKTU(client):
        emot = await get_vars(client.me.id, "EMOJI_WAKTU")
        emot_ji = emot if emot else "5440621591387980068"
        if client.me.is_premium:
            mmk = f"<emoji id={emot_ji}>🃏</emoji> "
        else:
            mmk = ""
        return mmk

    async def PASIR(client):
        emot_12 = await get_vars(client.me.id, "EMOJI_PASIR")
        emot_psr = emot_12 if emot_12 else "5258113901106580375"
        if client.me.is_premium:
            _pasir = f"<emoji id={emot_psr}>⌛</emoji> "
        else:
            _pasir = ""
        return _pasir
