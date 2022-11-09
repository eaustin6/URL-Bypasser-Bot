from sapling import SaplingClient
from bot import app
from pyrogram import filters

api_key = 'SFX8874YHNTDT880RDZIE5TMVDHV3Q8R'
client = SaplingClient(api_key=api_key)

def correctgm(text):
    data = list()
    try:
        for _ in client.edits(text, session_id='test_session'):
            data.append(_["sentence"])
    except:
        return None
    return data


@app.on_message(filters.command('grammar'))
def grammarcorrect(_, message):
    try:
        data = correctgm(message.text.split()[1])
        for _ in data:
            message.reply_text(_)
    except:
        return message.reply_text("No errors found in the sentence")
