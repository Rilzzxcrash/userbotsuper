from PyroUbot.core.database import mongo_client

db = mongo_client["terbaru"]
user_collection = db["user_dia"]

async def get_user_ids(client_id: int):
    user_ids = await user_collection.find_one({"_id": client_id})
    return user_ids["user_dia"] if user_ids else []