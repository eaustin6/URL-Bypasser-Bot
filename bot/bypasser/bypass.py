from bot import app
from pyrogram import filters
import PyBypass as bypasser


@app.on_message(filters.command('bypass'))
def bypass(_, msg):
    if msg.reply_to_message:
        url = msg.reply_to_message.text
        if len(msg.text.split())>1:
            nam = msg.text.split()[1]
        else:
            nam = None
    else:
        try:
            url = msg.text.split()[1]
            try:
                nam = msg.text.split()[2]
            except:
                nam=None
        except:
            return msg.reply_text("Please Reply to a Url")

    x = msg.reply(f"Bypassing __`{url}`__...")

    try:
        bypassed = bypasser.bypass(url)
        if name:
            bypassed = bypasser.bypass(url, name=nam)
    except Exception as e:
        return msg.reply(e)

    x.delete()
    msg.reply_text(f"**BYPASSED URL:** `{bypassed}`")
