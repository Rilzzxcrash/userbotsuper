import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "7853215553").split()))

API_ID = int(os.getenv("API_ID", "25546347"))

API_HASH = os.getenv("API_HASH", "ffd96679fb5f663c7b2b67addf8daadb")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7564096959:AAHe_hGMNkx-Z8aTAK2xpPD7VUSmr7IbRk8")

OWNER_ID = int(os.getenv("OWNER_ID", "7853215553"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ml9079716:48gxGsQhTHWumLI15@cluster0.6e1q9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002331639417"))
