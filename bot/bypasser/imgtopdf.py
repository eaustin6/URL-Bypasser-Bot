import glob
import requests
import img2pdf
from bot import app
from pyrogram import filters
import os


def save(imgurl, filename):
    img_data = requests.get(imgurl).content
    with open(filename+".jpg", 'wb') as handler:
        handler.write(img_data)

@app.on_message(filters.command('imgtopdf'))
def convertPDF(_, message):
    msg = message.text.split("&")
    data= msg[1].replace("['", "").replace("']", "").replace(";", "").split("', '")
    name = msg[2]
    print("Before", os.listdir())
    print(data, name)
    for _ in data:
        flnm=f"{name}/{data.index(_)}"
        print(flnm)
        save(_, flnm)
        
    print("After", os.listdir())
    with open(f"{name}s.pdf","wb") as f:
        f.write(img2pdf.convert(glob.glob(f"{name}/*.jpg")))
    message.reply_document(f"{name}s.pdf")
