f = open("9 task/9.csv")

cnt = 0

for i in f:
    i = sorted(list(map(int, i.split(","))))
    chk1 = False
    chk2 = False
    
    if (i[0] + i[-1]) % 3 == 0:
        chk1 = True 
    
    if (i[-1] - i[1] == i[-2] - i[0]) or (i[-1] - i[-2] == i[1] - i[0]):
        chk2 = True
    
    if chk1 and chk2:
        cnt += 1
        
print(cnt) 