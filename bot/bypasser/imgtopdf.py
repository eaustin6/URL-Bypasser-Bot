import glob
import requests
import img2pdf
from bot import app
from pyrogram import filters


def save(imgurl, filename):
    img_data = requests.get(imgurl).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)

@app.on_message(filters.command('imgtopdf'))
def convertPDF(_, message):
    data= message.text.split()[1]
    name = message.text.split()[2]
    
    try:
        for _ in data.replace("['", "").replace("']", "").split("', '"):
            save(_, f"{name}/{data.index(_)}")
    except:
        message.reply("Please enter valid data")
        
    with open(f"{name}s.pdf","wb") as f:
        f.write(img2pdf.convert(glob.glob(f"{name}/*.jpg")))
    message.reply_document(f"{name}.pdf")
