#!/usr/bin/python3

import base64
import json
from pathlib import Path
from urllib.request import urlopen

path = Path(__file__).parent
file = open(str(path.joinpath('config/config.json')), 'r')
config = json.load(file)

html = open(str(path.joinpath('../web/index.html')), 'r').read()

ip = urlopen("http://ifconfig.io/ip").read().decode().rstrip()

for inbound in config['inbounds']:
    if inbound['protocol'] == 'socks':
        port = str(inbound['port'])
        print("\nSOCKS: ")
        print("127.0.0.1:{}".format(port))
    if inbound['protocol'] == 'http':
        port = str(inbound['port'])
        print("\nHTTP: ")
        print("127.0.0.1:{}".format(port))
    if inbound['protocol'] == 'shadowsocks':
        port = str(inbound['port'])
        method = inbound['settings']['method']
        password = inbound['settings']['password']
        security = base64.b64encode((method + ":" + password).encode('ascii')).decode('ascii')
        link = "ss://{}@{}:{}#{}:{}".format(security, ip, port, ip, port)

        print("\nShadowsocks/Outline: ")
        print(link)

        html = html.replace("ss://proxy#name", link)
    if inbound['protocol'] == 'vmess':
        port = str(inbound['port'])
        uuid = inbound['settings']['clients'][0]['id']
        security = inbound['settings']['clients'][0]['security']
        ps = "{}:{}".format(ip, port)

        c = {"add": ip, "aid": "0", "host": "", "id": uuid, "net": "tcp", "path": "", "port": port, "ps": ps,
             "tls": "none", "type": "none", "v": "2"}
        j = json.dumps(c)
        link = "vmess://" + base64.b64encode(j.encode('ascii')).decode('ascii')

        print("\nVMESS: ")
        print(link)

        html = html.replace("vmess://etc", link)

open(str(path.joinpath('../web/index.html')), 'w').write(html)
