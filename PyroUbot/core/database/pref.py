from PyroUbot.core.database import mongodb

prefixes = mongodb["PyroUbot"]["prefix"]

async def get_pref(user_id: int):
    sh = await prefixes.find_one({"_id": user_id})
    if sh:
        return sh.get("prefixesi")
    else:
        return "."

async def set_pref(user_id: int, prefix: str):
    await prefixes.update_one(
        {"_id": user_id}, {"$set": {"prefixesi": prefix}}, upsert=True
    )

async def rem_pref(user_id: int):
    await prefixes.update_one(
        {"_id": user_id}, {"$unset": {"prefixesi": ""}}, upsert=True
    )