f = open("9 task/9.csv")
cnt = 0

for i in f:
    i = sorted(map(int, i.split(";")))

    if i[-1] < i[0] + i[1] + i[2] and i[-1] + i[0] != i[1] + i[2]:
        cnt += 1

print(cnt)
