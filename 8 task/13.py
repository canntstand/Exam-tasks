from itertools import product

s = sorted("ГИРЛЯНДА")
cnt = 0

for i in product(s, repeat=9):
    if i.count("А") == 1:
        index = i.index("А")
        if index == 0:
            if i[1] not in "ГРЛНД":
                cnt += 1
        elif index == 8:
            if i[-2] not in "ГРЛНД":
                cnt += 1
        else:
            if i[index - 1] not in "ГРЛНД" and i[index + 1] not in "ГРЛНД":
                cnt += 1

print(cnt)