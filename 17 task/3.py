f = open("17 task/17.txt")
cnt = 0

l = [i for i in f]

for i in range(len(l)):
    if i < len(l) - 1:
        if ("-" in l[i] and "-" in l[i + 1]) or ("-" not in l[i] and "-" not in l[i + 1]):
            cnt += 1
        
print(cnt)