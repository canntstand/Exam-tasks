f = open("9 task/9.csv")
cnt = 0

for i in f:
    i = sorted(list(map(int, i.strip().split(";"))))

    if (i[-1] < (i[0] + i[1] + i[2])) and ((i[-1] + i[0]) != (i[-2] + i[1])):
        print(i)
        cnt += 1

print(cnt)
