
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
import json
import subprocess

import uuid
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

def genuri():
    email="EMAILsO"+''.join(random.choices(string.ascii_uppercase, k=5))+"O@MAIL.COM"
    id=str(uuid.uuid4())
    newClient=    {
        "id": id,
        "flow": "xtls-rprx-direct",
        "email": email,
        "limitIp": 0,
        "totalGB": 0,
        "expiryTime": ""
    }
    inbund_sttings = models.Inbounds.objects.get(id=1)
    data=inbund_sttings.settings
    data=json.loads(data)
    data["clients"].append(newClient)
    data=json.dumps(data)
    models.Inbounds.objects.filter(id=1).update(settings=data)
    a = models.InboundClientIps(client_email = email, ips = "[]")
    a.save()
    a = models.ClientTraffics(inbound_id=1,enable=1,email=email,up=0,down=0,expiry_time=0,total=0)
    a.save()
    #uri="vless://"+id+"@"+"172.67.191.189"+":443?path=%2F&security=tls&encryption=none&host=vs02up.gozaraztah.store&type=ws&sni=vs02up.gozaraztah.store#🇩🇪-S2up"
    uri="vless://"+id+"@brtg234.gozaraztah.store:1356?type=ws&security=tls&path=%2Fvar%2Fwww%2Fmeow&sni=brtg234.gozaraztah.store#brtg234[SINGLEUSER](vless%2Btls%2Bws)"
    return uri

@api_view()
def geturi(request):

    uri=genuri()
    return Response(uri)

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
                uri+=[genuri()]
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
    
@api_view()
def xuiRestart(request):
    #telId userCount
    try:
        subprocess.Popen('x-ui restart', shell=True)
        data={'success':'1',"msg":"x-ui has been successfully restarted"}
    except Exception as e:
        data={'success':'0',"msg":str(e)}

    return Response(data)
    
 

    
    

