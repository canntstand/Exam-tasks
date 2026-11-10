from ipaddress import *

for mask in range(0, 33):
    net1 = ip_network(f"10.227.3.113/{mask}", 0)
    net2 = ip_network(f"10.235.127.7/{mask}", 0)
    if net1 != net2:
        print(net1, net2)