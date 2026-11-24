from itertools import *

s = "012345678"
cnt = 0

for i in product(s, repeat=7):
    i = "".join(i)
    
    if i[0] not in "246" and len(set(i[-3:])) != 1 and i[0] != "0":
        cnt += 1

print(cnt)