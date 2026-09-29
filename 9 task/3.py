f = open("9 task/1_9.txt")
cnt = 0
for i in f:
    i = sorted(list(map(int, i.split())))
    if len(set(i)) == len(i) and i[-1] + i[-2] <= i[0] + i[1] + i[2]:
        cnt += 1

print(cnt)
