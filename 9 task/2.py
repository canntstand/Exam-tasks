f = open("9.txt")
ans = 0
for i in f:
    i = sorted(list(map(int, i.split())))
    cnt = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for j in i:
        if i.count(j) == 3 and len(set(i)) == 4:
            cnt2 = 1
        
        if i[-1] + i[-2] > (i[0] + i[1] + i[2] + i[3]) * 2:
            cnt3 = 1
        
        if j % 2 == 0:
            cnt += 1
        
        if cnt > 3:
            cnt1 = 1
    
    if cnt1 + cnt2 + cnt3 >= 2:
        ans += 1

print(ans)