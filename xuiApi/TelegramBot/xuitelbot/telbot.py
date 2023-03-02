from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, Message
import json
import os
# Secrets
import time 
import requests
import ast
import urllib.parse

#with open("Secret.json") as fp:
#    sec = json.load(fp)

app = Client(
	"v2ray_bot",
	api_id = '1029037',
	api_hash = 'ffb67d45441d83512348881f6b69e3ed',
	bot_token="5990771248:AAE5-1qakfJjULCicoI1BP7e9Ol7-GKQZg0",

    )

@app.on_message(filters.command("start"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text="سلام به ربات خوش اومدین برای اشنایی با ربات /help را وارد کنید:)")

@app.on_message(filters.command("help"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text="دریافت کانفیگ ها /getconfigs \n برای اطاعات توسعه دهنده /aboutdev \n آموزش استفاده /howToUseConfigs \n /myid جهت دریافت ایدی تلگرام خودتون")


@app.on_message(filters.command("aboutdev"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text="یه دولپر هاهاهاهاها :)))")

@app.on_message(filters.command("myid"))
def start_handler(client, message):
    # do something
    client.send_message(chat_id=message.chat.id, text=message.chat.id)

@app.on_message(filters.command("howToUseConfigs"))
def start_handler(client, message):
    # do something
    data="آموزش استفاده در کلاینت(گوشی لپتاپ سیستم عامل)  مختلف در کانال @mmdofhowto قرار دارد."
    client.send_message(chat_id=message.chat.id, text=data)



@app.on_message(filters.command("getconfigs"))
def start_handler(client, message):
    responcedata=''
    user_id = message.chat.id
    endPoint='http://api.gozaraztah.store:8001/api/telegram/geturi/'+str(user_id)
    responce= requests.get(endPoint)
    responceJson=responce.json()

    if(responceJson["success"]=='1'):
        if (int(responceJson["delta"])!=0):
            data="به کانفیگ های شما به تعداد"+responceJson["delta"]+"اضافه شد این کانفیگ جدید حد اکثر تا ۵ دقیقه اینده فعال میشود"
            client.send_message(chat_id=message.chat.id, text=data)
        if(responceJson["new"]=="1" and int(responceJson["delta"])==0):
            data="\n برای دریافت کانفیگ مجددا /getconfigs  تا فعال شدن کانفیگ های خود حد اکثر <b> ۵ دقیقه </b> صبر کنید"
            client.send_message(chat_id=message.chat.id, text=data)
        #userathenticated            
        uriList = responceJson["uri"]
        uriList = ast.literal_eval(uriList)
        msg="تعداد کافیگ های شما"+str(len(uriList))
        


        client.send_message(chat_id=message.chat.id, text=msg)
        for uri in uriList:
            client.send_message(chat_id=message.chat.id, text="<code>"+uri+"</code>"+"\n"+'<a href="https://qr-code.ir/api/qr-code/?d='+urllib.parse.quote(uri)+'">مشاهده کبوآر کد کانفیگ</a>')

        if(responceJson["new"]=="0"):
            data='کانفیگ های ثبت شده شما مجددا ارسال شد '
            client.send_message(chat_id=message.chat.id, text=data)


    if(responceJson["success"]=='69'):
        responcedata="خطای ۶۹ \n حساب کاربری شما یافت نشد \n (اگر ثبت سفارش کرده اید و با این خطا رو به رو می شوید با ادمین تماس بگیرید)"
        client.send_message(chat_id=message.chat.id, text=responcedata)

    


    







@app.on_message(filters.text)
def retreive_text(c, msg: Message):
    # User Id 
    user_id = msg.chat.id
    # User Name 
    user_name = msg.chat.username  

    app.send_message(
        msg.chat.id,  # Change this to your username or id
        " /help را وارد کنید سلام خوش اومدین میخواین کانفیگ دریافت کنید؟"
    )

app.run()
