
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
import json
import subprocess

import uuid
import random
import string
from sequences import get_next_value
from ast import literal_eval

import requests
import re



def genuri():
   # server_EndPoint=['http://46.245.76.234:8000/api/geturi/','http://31.7.76.105:8000/api/geturi/','http://109.122.199.26:8000/api/geturi/']
    server_EndPoint=['http://109.122.199.26:8000/api/geturi/']
    server_number=get_next_value("server", initial_value=0, reset_value=len(server_EndPoint))
    
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
            urilist=literal_eval(user_uri.user_id)
            user_uri_count=int(user.client_count)
            #equal
            if(len(urilist)==user_uri_count):
                uri={"uri":user_uri.user_id,'success':'1',"new":"0","delta":0}
            #increse
            if(len(urilist)<user_uri_count):
                delta=user_uri_count-len(urilist)
                for x in range(delta):
                    urilist+=[genuri()['uri']]
                    q = models.UsersUri(telegram_id=user, user_id=urilist)
                    q.save()
                uri={"uri":user_uri.user_id,'success':'1',"new":"1","delta":str(delta)}
                


        else:
            
            for x in range(int(user.client_count)):
                uri+=[genuri()['uri']]
            q = models.UsersUri(telegram_id=user, user_id=uri)
            q.save()
            uri={"uri":str(uri),'success':'1',"new":"1","delta":0}

    else:
        uri={"uri":"kir","success":"69","new":"kosMadarKameneii","delta":0}

    return Response(uri)
    
@api_view()
def addTelegramUseer(request,telId,userCount):
    #telId userCount
    try:
        q = models.TelegramUsers(telegram_id=telId, client_count=userCount)
        q.save()
        data={'success':'1',"msg":"user has been successfully added/updated"}
    except Exception as e:
        data={'success':'0',"msg":str(e)}

    return Response(data)
    
@api_view()
def deluri(request,domain):
    pattern = r'@(.*):'
    mmd=''

    all_records = models.UsersUri.objects.all()

    for record in all_records:
        urilist=literal_eval(record.user_id)

        for uri_list in urilist :
            string =uri_list
            # return Response({str(type(string)):str(string)})
            match = re.search(pattern, string)
            if match[1]==domain:
                urilist.remove(string)

        record.user_id=str(urilist)
        record.save()

    

                
                



    return Response({"txt":mmd})

    

