from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, Message
import json
import os
# Secrets
import time 
import requests
import ast

#with open("Secret.json") as fp:
#    sec = json.load(fp)

app = Client(
	"v2ray_bot",
	api_id = '1029037',
	api_hash = 'ffb67d45441d83512348881f6b69e3ed',
	bot_token="6073845735:AAH251rPL1bbUlxEsrzNtQxWozBG4PjUjNA",

    )

"""
@app.on_message(filters.text)
def voi(c, msg: Message):
    app.send_message(
        msg.chat.id,  # Change this to your username or id
        "دریافت کانفیگ؟",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("آره بابا خرابه!!!", msg.chat)]]
        )
    )

"""

#app.send_message(
#        msg.chat.id,  # Change this to your username or id
#        "سلام خوش اومدین میخواین کانفیگ دریافت کنید؟",
#        reply_markup=InlineKeyboardMarkup(
#            [[InlineKeyboardButton("بله", msg.chat)]]
#        )
#    )





@app.on_message(filters.command("start"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text="سلام به ربات خوش اومدین برای اشنایی با ربات /help را وارد کنید:)")

@app.on_message(filters.command("help"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text="دریافت کانفیگ ها /getconfigs \n برای اطاعات توسعه دهنده /aboutdev \n /myid جهت دریافت ایدی تلگرام خودتون")


@app.on_message(filters.command("aboutdev"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text="یه دولپر هاهاهاهاها :)))")

@app.on_message(filters.command("myid"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text=message.chat.id)


@app.on_message(filters.command("getconfigs"))
def start_handler(client, message):
    responcedata=''
    user_id = message.chat.id
    user_id=87
    endPoint='http://api.gozaraztah.store:8001/api/telegram/geturi/'+str(user_id)
    responce= requests.get(endPoint)
    responceJson=responce.json()

    if(responceJson["success"]=='1'):

        if(responceJson["new"]=="1"):
            data="\n برای دریافت کانفیگ مجددا/getconfigs  تا فعال شدن کانفیگ های خود حد اکثر ۵ دقیقه صبر کنید"
            client.send_message(chat_id=message.chat.id, text=data)
        #userathenticated            
        uriList = responceJson["uri"]
        uriList = ast.literal_eval(uriList)
        msg="تعداد کافیگ های شما"+str(len(uriList))
        


        client.send_message(chat_id=message.chat.id, text=msg)
        for uri in uriList:
            client.send_message(chat_id=message.chat.id, text=uri)

        if(responceJson["new"]=="0"):
            data='کانفیگ های ثبت شده شما مجددا ارسال شد '
            client.send_message(chat_id=message.chat.id, text=data)


    if(responceJson["success"]=='69'):
        responcedata="خطای 69 \n حساب کاربری شما ثیت نشده است"
        client.send_message(chat_id=message.chat.id, text=responcedata)
  
    


    







@app.on_message(filters.text)
def retreive_text(c, msg: Message):
    # User Id 
    user_id = msg.chat.id
    # User Name 
    user_name = msg.chat.username  

    app.send_message(
        msg.chat.id,  # Change this to your username or id
        "سلام خوش اومدین میخواین کانفیگ دریافت کنید؟"
    )
    #    reply_markup=InlineKeyboardMarkup(
    #        [[InlineKeyboardButton("بله", msg.chat)]]
    #    )
    #)    
    #print(msg)

# @app.on_message(filters.command(["/config"]))
# async def my_handler(client, message):
#     # Api req goes here 
    
#     print('This is the /config command')

app.run()