from bot import app
from pyrogram import filters
import PyBypass as bypasser


@app.on_message(filters.command('bypass'))
def bypass(_, msg):
    if msg.reply_to_message:
        url = msg.reply_to_message.text
    else:
        try:
            url = message.text.split[1]
        except:
            return message.reply_text("Please Reply to a Url")
    
    try:
        message.reply_text(bypasser.bypass(url))
    except Exception as e:
        message.reply(e)
    
