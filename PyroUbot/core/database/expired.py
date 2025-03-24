from PyroUbot.core.database import mongo_client

userEXP = mongo_client["PyroUbot"]["users"]

async def get_expired_date(user_id: int):
    user = await userEXP.users.find_one({"_id": user_id})
    if user:
        return user.get("expire_date")
    else:
        return None

async def set_expired_date(user_id: int, expire_date: int):
    await userEXP.users.update_one(
        {"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True
    )

async def rem_expired_date(user_id: int):
    await userEXP.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )