from bot import app
import logging
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton as Ikb
from pyrogram.types import InlineKeyboardMarkup as Ikm

HOWITWORKS = "IDK"
telegraph_url=""
mrkup=Ikm([
                [Ikb(text="📞Support", url="t.me/ShinobuSupport"),
                 Ikb(text="⚙️Supported Link", url=telegraph_url)]
                [Ikb(text="How It Works", callback_data="how_it_works")]
             ])

@app.on_message(filters.command(["start", "help"]))
async def start(_, message):
    text = f"Hi! {message.from_user.first_name}\nI am a Simple bypasser bot\nJust Send me a link and I'll bypass it for you!)
    await message.reply_text(text, reply_markup=mrkup)




@app.on_callback_query(filters.regex("how_it_works"))
async def helpcback(_, query):
    await query.edit_message_text(text=HOWITWORKS, reply_markup=mrkup, parse_mode = "md")


def alive():
    app.run()
    app.send_message(-1001207787457, "I'm alive!")
     
  
if __name__=="__main__":
    alive() 

