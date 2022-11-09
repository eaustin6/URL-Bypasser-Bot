import requests
from bot import app
from pyrogram import filters

def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = requests.post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"

@app.on_message(filters.command('paste'))
def pastewo(_, message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = message.text.split()[1]
    return paste(text)
