from itertools import *

s = "ABCWXYZ"
cnt = 0

for i in product(s, repeat=6):
    if i[0] in "WXYZ" and i[-1] in "WXYZ" and all(x not in "WXYZ" for x in i[1:-1]):
        cnt += 1

print(cnt)