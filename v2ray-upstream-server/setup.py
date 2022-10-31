#!/usr/bin/python3

import uuid
from pathlib import Path
from urllib.request import urlopen

path = Path(__file__).parent.joinpath('config/config.json')
config = open(str(path), 'r').read()

upstreamUUID = input("Upstream UUID: (Leave empty to generate a random one)\n")
if upstreamUUID == "":
    upstreamUUID = str(uuid.uuid4())

config = config.replace("<UPSTREAM-UUID>", upstreamUUID)
open(str(path), 'w').write(config)

ip = urlopen("http://ifconfig.io/ip").read().decode().rstrip()

print('Upstream IP: ' + ip)
print('Upstream UUID:')
print(upstreamUUID)
