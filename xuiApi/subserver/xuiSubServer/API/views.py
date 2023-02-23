from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
import json
import subprocess

import uuid
import random
import string
# Create your views here.

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
        "limitIp": 2,
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

    #############
    serverdomain="brtg234.gozaraztah.store"
    sni="brtg234.gozaraztah.store"
    serverport='1356'
    serverWSpath="%2Fvar%2Fwww%2Fmeow"
    config_txt="brtg234[SINGLEUSER]"
    #####################

    uri="vless://"+id+"@"+serverdomain+":"+serverport+"?type=ws&security=tls&path="+serverWSpath+"&sni="+sni+"#"+config_txt+""


    return uri





@api_view()
def geturi(request):

    uri=genuri()
    return Response(uri)


