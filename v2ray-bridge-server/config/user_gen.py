import email
import json
import uuid
import base64
import socket
import pyqrcode



with open('config.json', 'r') as openfile:
    json_object = json.load(openfile)



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip=s.getsockname()[0]
s.close()


name=input("name=>")
servername="hkhkhkhi"
Port=input("Port=>")
connection_type=input("connection type=>")


email=name+"@"+servername+".meow"
uuid=str(uuid.uuid4())

new_User={"id": uuid, "alterId": 0, "security": "none", "email":email}
json_object['inbounds'][3]['settings']['clients'].append(new_User)

json_object=json.dumps(json_object, sort_keys=True, indent=4)

#Writing to sample.json
with open("config.json", "w") as outfile:
    outfile.write(str(json_object))


USER_JSON={
  "add": server_ip,
  "aid": "0",
  "host": "",
  "id": uuid,
  "net": connection_type,
  "path": "",
  "port": Port,
  "ps": name,
  "sni": "",
  "tls": "",
  "type": "",
  "v": "2"
}


sample_string = str(USER_JSON)
sample_string_bytes = sample_string.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")



print("======================================================================================================")
print()

uri="vmess://"+base64_string

print(uri)
print()
print()


url = pyqrcode.create(uri)
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))


print()
print("======================================================================================================")
