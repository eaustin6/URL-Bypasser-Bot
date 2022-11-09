from bot import app
from pyrogram import filters

BANNED_URLS = ["pornhub", "pornhub.com", "xhamster", "xHamster.com", "nhentai", "nhentai.com", "iporn", "xvideo", "xvideos", "por", "orn", "nude", "xxx"]

@app.on_message(filters.command("webss"))
async def take_ss(_, message):
    try:
        if len(message.command) != 2:
            return await message.reply_text("Give A Url To Fetch Screenshot.")
        url = message.text.split(None, 1)[1]
        await app.send_message(720518864, f"#WEBSS\n\nUser: {message.from_user.mention}\nURL: {url}")
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except:
            return await m.edit("No Such Website.")
        await m.delete()
    except Exception as e:
        await message.reply_text("Unknown Error Occurred")
