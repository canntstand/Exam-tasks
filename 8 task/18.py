from itertools import *

s = "ГЕПАРД"
cnt = 0

for i in product(s, repeat=5):
    if i.count("Г") == 1 and i[0] != "А" and i[-1] != "Е":
        cnt += 1
        
print(cnt)