from bot import telegraph, logger, app
from pyrogram import filters
import os


def convertTelegraph(data, datatype):
    if datatype==
    post_content = "".join(f"<img src={link}><br>" for link in data)
    post = telegraph.create_page(
        nam,
        html_content=post_content,
    )
    try:
        return post["url"]
    except:
        x = convertTelegraph(data, nam=nam)
        return x


@app.on_message(filters.command("tgt"))
async def graphoo(_, msg):
    """function"""
    
    user = msg.from_user
        try:
            title = user.first_name
        except:
            title = "@URLBypasserBot"
            
    if msg.reply_to_message:
        content = msg.reply_to_message
        x = msg.reply_text(f"Pasting {content.link} to telegraph!")
        
        if content.text:
            text = content.text
            
        if content.document and (content.document.file_size<(10 * 1024**2)):
            
            try:
                path = await content.download()
                with open(path) as data:
                    text = data.read()
                os.remove(path)
                
            except Exception as e:
                logger.error(e, "caused by FUNC: graphoo")
                await msg.reply_text(f"Sorry some error excured\nERROR: {e}")
                x.delete()
                return
        
        else:
            await msg.reply_text("Please Reply to a Text or Document")
            x.delete()
            return
    
    else:
        x = msg.reply_text(f"Pasting {msg.link} to telegraph!")
        
        m = msg.text.split()
        if len(m)<2:
            await msg.reply_text("Format: /tgt <reply_to_msg/text>", parse_mode="markdown")
            x.delete()
            return
        text = m[1]
    
    text = text.replace("\n", "<br>")
    
    try:
        response = await telegraph.create_page(
                title,
                html_content=text
            )
    except Exception as e:
        logger.error(e, "caused by FUNC: graphoo")
        await msg.reply_text(f"Telegraph is not responding\nERROR: {e}")
        x.delete()
        return
        
    
    await msg.reply_text("Pasted to [Telegraph](https://graph.org/{})".format(response["path"]))

    x.delete()
