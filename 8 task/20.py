from itertools import *

s = "0123456"
cnt = 0

for i in product(s, repeat=6):
    i = "".join(i)

    if i.count("6") == 1 and i[0] != "0" and (
        all(int(i[x]) % 2 == 0 if x % 2 == 0 else int(i[x]) % 2 != 0 for x in range(6))
        or all(int(i[x]) % 2 != 0 if x % 2 == 0 else int(i[x]) % 2 == 0 for x in range(6))
    ):
        cnt += 1

print(cnt)
