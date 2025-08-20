import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "1674869955").split()))

API_ID = int(os.getenv("API_ID", "28092374"))

API_HASH = os.getenv("API_HASH", "ddb82b3f2519a5bc54510b7caa176431")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8296574253:AAFInS_Dw49wk4QgcZIpZ9blSXaSeSeAYYU")

OWNER_ID = int(os.getenv("OWNER_ID", "1674869955"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://briandinda1235:vMgM8VWt33zvDkX@cluster0.u2pldih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002962949016"))
