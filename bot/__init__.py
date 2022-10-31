from pyrogram import Client
import os

API_ID = int(os.environ.get("ID"))
API_HASH = str(os.environ.get("HASH"))
BOT_TOKEN = str(os.environ.get("TOKEN"))

GDTOT_CRYPT = str(os.environ.get("GDTOT_CRYPT", ""))
APPDRIVE_EMAIL = str(os.environ.get("APPDRIVE_EMAIL", ""))
APPDRIVE_PASSWORD = str(os.environ.get("APPDRIVE_PASSWORD", ""))
HUBDRIVE_CRYPT = str(os.environ.get("HUBDRIVE_CRYPT", ""))
sharerepw_xsrf_token, sharerpw_larvel_token = "", ""


print("[INFO] Starting Pyrogram Instance")
app = Client("app", bot_token=BOT_TOKEN, 
                    api_id=API_ID,
                    api_hash=API_HASH,
                    plugins=dict(root=bypasser/"))
