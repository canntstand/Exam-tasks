from itertools import product

s = "ГИПЕРБОЛА"
vow = "ИЕОА"
cons = "ГПРБЛ"

cnt = 0

for i in product(s, repeat=6):
    if (
        i[0] not in vow
        and i[-1] not in vow
        and not (i[1] in vow and i[0] in cons and i[2] in cons)
        and not (i[2] in vow and i[1] in cons and i[3] in cons)
        and not (i[3] in vow and i[2] in cons and i[4] in cons)
        and not (i[4] in vow and i[3] in cons and i[5] in cons)
    ):
        cnt += 1

print(cnt)
