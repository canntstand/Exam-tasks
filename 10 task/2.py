from ipaddress import *

net = ip_network("176.112.100.128/255.255.255.224", 0)
cnt = 0

for i in net:
    i = "".join(list(map(lambda x: bin(int(x))[2:], str(i).split("."))))
    if i.count("1") % 2 != 0:
        cnt += 1

print(cnt)
    