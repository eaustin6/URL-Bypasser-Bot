import os
from bot import app
from pyrogram import filters



@app.on_message(filters.command('rename'))
def rename(_, message):
    if not message.reply_to_message:
        message.reply("Please reply to a file/document")
    try:
        filename = message.text.replace(message.text.split(" ")[0], "")
    except Exception as e:
        print(e)
    reply = message.reply_to_message
    if reply:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)



@app.on_message(filters.command("tgupload"))
def tgupload(_, msg):
    if msg.reply_to_message:
        address = msg.reply_to_message.text
        
    else:
        try:
            address = msg.text.split()[1]
        except:
            return msg.reply_text("Please Reply to a Url")
    
    x = msg.reply_text("Uploading to telegram...")
    try:
        if address.startswith("http"):
            if address.endswith(".jpg") or address.endswith(".png") or address.endswith(".jpeg"):
                message.reply_photo(address)
                message.reply_document(address)
            elif address.endswith(".mp4") or address.endswith(".mkv") or address.endswith(".mov"):
                if len(msg)>2:
                    message.reply_document(address)
                else:
                    message.reply_video(address)
            else:
                message.reply_document(address)
        else:
            if True:
                message.reply_document(address)
        x.delete()
    except:
        message.reply("No such File/Directory/Link")
