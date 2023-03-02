import requests
list=[[579759230,1],[499296795,2],[103195411,5],[1915468300,3],[886482324,1],[1980575291,2],[395350930,3],[133981684,1],[142479814,4],[584067324,1],[1434937851,2],[1325197056,1],[434702477,1],[124143038,2],[448686996,9]]
urls=[]
for l in list:
    urls+=['http://api.gozaraztah.store:8001/api/telegram/addnewuser/'+str(l[0])+'/'+str(l[1])+'/']
    
for url in urls:
    r = requests.get(url = url) 
    data = r.json()
    print(data)
    
