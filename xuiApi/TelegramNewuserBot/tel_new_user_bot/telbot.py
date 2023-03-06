from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, Message
import json
import os

import time 
import requests
import ast
import urllib.parse

app = Client(
	"v2ray_adduser_bot",
	api_id = '1029037',
	api_hash = 'ffb67d45441d83512348881f6b69e3ed',
	bot_token="5989987120:AAFaTGGQwnbZ1quW02w67ZcHdgVxHXas_ww",

    )

@app.on_message(filters.text)
def retreive_text(c, msg: Message):
    list=ast.literal_eval(msg)
 
    for l in list:
        url='http://api.gozaraztah.store:8001/api/telegram/addnewuser/'+str(l[0])+'/'+str(l[1])+'/'
        r = requests.get(url) 
        data = r.json()
        app.send_message(msg.chat.id,str(data))

    app.send_message(msg.chat.id,"done")
app.run()

 
