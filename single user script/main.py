import os
import re

my_file = open("acsess.log", "r")
data = my_file.read()
my_file.close()
#deleteling file

# if os.path.exists("acsess.log"):
#   os.remove("acsess.log")
# else:
#   pass

data_list = data.split("\n")
data_dict={}
for data in data_list:
    x = re.findall("\d*\/\d*\/\d* \d*:\d*:\d* (\d*.\d*.\d*.\d*):\d* .* email: (.*@.*\..*)", data)
    #print(x)
    try :
        email=x[0][1]
        ip=x[0][0]
        if email in data_dict:
            if not ip in data_dict[email]:
                data_dict[email]+=[ip]
            else:
                pass
        else:
            data_dict[email]=[ip]
    except:
        pass

for data in data_dict:
    data_dict[data]=len(data_dict[data])

print(data_dict)


