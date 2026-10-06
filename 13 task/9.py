def f(s, e):
    if s == e: return 1
    if s > e: return 0
    
    return f(s + 1, e) + f(s * 2, e) + f(s * 3, e)

cnt = 0

for i in range(1, 15):
    out = f(i, 15) 
    if i % 2 == 0:
        cnt += out

print(cnt)