from bot import app
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton as Ikb, InlineKeyboardMarkup as Ikm

telegraph_url=""
telegrapho_url=""
mrkup=Ikm([
                [Ikb(text="📞Support", url="t.me/ShinobuSupport"), Ikb(text="⚙️Supported Link", url=telegraph_url)],
                [Ikb(text="How It Works", url=telegrapho_url)]
             ])

@app.on_message(filters.command(["start", "help"]))
async def start(_, message):
    text = f"*Hi! {message.from_user.first_name}*\n\n*I am a Simple url bypasser bot*\n\n*Just Send me a link and Ill bypass it for you!*"
    await message.reply_text(text, reply_markup=mrkup)



def alive():
    app.run()
    app.send_message(-1001207787457, "I'm alive!")
     
  
if __name__=="__main__":
    alive() 

