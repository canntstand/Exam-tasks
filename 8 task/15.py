from itertools import *

cnt = 0

for i in product(sorted("МАРИЯ"), repeat=4):
    cnt += 1
    if "".join(i) == "АРИЯ":
        print(cnt)
        break