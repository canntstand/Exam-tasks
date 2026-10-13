f = open("17 task/17.txt")
l = []
cnt = 0

for i in f:
    l.append(int(i))
    
for i in range(len(l)):
    if i + 1 < len(l):
        if l[i] >= 0 and l[i + 1] >= 0 or l[i] < 0 and l[i + 1] < 0:
            cnt += 1
    
print(cnt)