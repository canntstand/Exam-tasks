f = open("9.txt")
n = 0
for i in f:
    n += 1
    i = sorted(list(map(int, i.split())))
    if len(set(i)) == len(i) and (i[0] + i[4]) * 2 < i[1] + i[2] + i[3]:
        print(n)
