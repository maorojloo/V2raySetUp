
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
import json
import subprocess

import uuid
import random
import string
from sequences import get_next_value

import requests




def genuri():

    server_number=get_next_value("server", initial_value=0, reset_value=2)
    server_EndPoint=['http://46.245.76.234:8000/api/geturi/','http://31.7.76.105:8000/api/geturi/']
    
    r = requests.get(url = server_EndPoint[server_number])
    
    data = r.json()

    data={"uri":data,"server_number":server_number}
    return(data)




@api_view()
def geturiTelegram(request,telId):
    uri=[]
    user=''
    user_uri=''

    try:
        user = models.TelegramUsers.objects.get(telegram_id=telId)
    except :
        user = False

    if (user):
        try:
            user_uri=models.UsersUri.objects.get(telegram_id=user)
        except :
            user_uri = False
        if(user_uri):
            uri={"ok",}
            uri={"uri":user_uri.user_id,'success':'1',"new":"0"}
        else:
            
            for x in range(int(user.client_count)):
                uri+=[genuri()['uri']]
            q = models.UsersUri(telegram_id=user, user_id=uri)
            q.save()
            uri={"uri":uri,'success':'1',"new":"1"}

    else:
        uri={"uri":"kir","success":"69","new":"kosMadarKameneii"}

    return Response(uri)
    
@api_view()
def addTelegramUseer(request,telId,userCount):
    #telId userCount
    try:
        q = models.TelegramUsers(telegram_id=telId, client_count=userCount)
        q.save()
        data={'success':'1',"msg":"user has been successfully added"}
    except Exception as e:
        data={'success':'0',"msg":str(e)}

    return Response(data)
    

    

