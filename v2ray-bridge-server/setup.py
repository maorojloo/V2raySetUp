#!/usr/bin/python3

import uuid
import secrets
from pathlib import Path
from urllib.request import urlopen

path = Path(__file__).parent.joinpath('config/config.json')
config = open(str(path), 'r').read()

upstreamUUID = input("Upstream UUID:\n")
upstreamIP = input("Upstream IP:\n")

bridgeUUID = input("Bridge UUID: (Leave empty to generate a random one)\n")
if bridgeUUID == "":
    bridgeUUID = str(uuid.uuid4())

ssPassword = input("Shadowsocks Password: (Leave empty to generate a random one)\n")
if ssPassword == "":
    ssPassword = secrets.token_urlsafe(16)

config = config.replace("<UPSTREAM-UUID>", upstreamUUID)
config = config.replace("<UPSTREAM-IP>", upstreamIP)
config = config.replace("<BRIDGE-UUID>", bridgeUUID)
config = config.replace("<SHADOWSOCKS-PASSWORD>", ssPassword)
open(str(path), 'w').write(config)

ip = urlopen("http://ifconfig.io/ip").read().decode().rstrip()

print('Done! Run ./clients.py to generate client links.')
