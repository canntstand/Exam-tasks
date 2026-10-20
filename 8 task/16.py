from itertools import product

s = sorted("АВЛОС")
num = 1

for i in product(s, repeat=4):
    if i[0] == "Л":
        print(num)
        break
    num += 1
