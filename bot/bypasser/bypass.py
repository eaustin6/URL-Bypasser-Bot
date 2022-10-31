from bot import app
from pyrogram import filters
import PyBypass as bypasser


@app.on_message(filters.command('bypass'))
def bypass(_, msg):
    if msg.reply_to_message:
        url = msg.reply_to_message.text
    else:
        try:
            url = msg.text.split()[1]
            try:
                name = msg.text.split()[2]
            except:
                None
        except:
            return msg.reply_text("Please Reply to a Url")

    x = msg.reply(f"Bypassing {url}...")

    try:
        bypassed = bypasser.bypass(url)
        if name:
            bypassed = bypasser.bypass(url, name=name)
    except Exception as e:
        return msg.reply(e)

    x.delete()
    msg.reply_text(f"**BYPASSED URL:** `{bypassed}`")
