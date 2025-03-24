from motor.motor_asyncio import AsyncIOMotorClient

from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.userbotxx

from PyroUbot.core.database.expired import *
from PyroUbot.core.database.userbot import *
from PyroUbot.core.database.pref import *
from PyroUbot.core.database.variabel import *
from PyroUbot.core.database.antigcast import *