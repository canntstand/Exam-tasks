from ipaddress import *

net = ip_network("16.128.15.3/255.255.224.0", False)

for i in net:
    print(i)
    
print(16 + 128 + 31 + 255)