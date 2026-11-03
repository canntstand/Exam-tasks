def f(l, x):
    if l[-1] >= 100 and x == 4: return True
    if l[-1] < 100 and x == 4: return False 
    if l[-1] >= 100: return False 
    
    l[-1] = l[-1] + l[-2]
    l.remove(l[-2])
    return f(l, x + 1)

ans = []

for s in range(14, 100):
    l = sorted([i for i in range(1, s + 1)])
    if f(l, 1):
        ans.append(s)

print(min(ans), max(ans))