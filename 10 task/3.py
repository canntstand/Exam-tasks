from ipaddress import *
ans = 0

for A in range(1, 256):
    net = ip_network(f"248.112.{A}.35/255.255.255.240", False)
    l = []
    
    for ip in net:
        ip = list(map(lambda x: bin(int(x))[2:].zfill(8), str(ip).split(".")))
        
        if ip[0].count("0") + ip[1].count("0") <= ip[2].count("0") + ip[3].count("0"):
            l.append(True)
        else:
            l.append(False)
    
    if all(l) and A > ans:
        ans = A

print(ans)