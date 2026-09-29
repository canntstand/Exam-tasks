from itertools import product

s = sorted("ПАРУС")
cnt = 0

for i in product(s, repeat=4):
    cnt += 1
    if i.count("А") == 0:
        print(cnt)
        break

