def f(l, x):
    l = sorted(l)
    
    if l[0] == l[1] and x == 4: return True
    if l[0] != l[1] and x == 4: return False
    if l[0] == l[1] and x != 4: return False
    
    if x % 2 == 0:
        return f([l[0] + 1, l[1]], x + 1) and f([l[0] + 3, l[1]], x + 1)
    else:
        return f([l[0] + 1, l[1]], x + 1) or f([l[0] + 3, l[1]], x + 1)
        

for s in range(1, 24):
    if f([13, s], 1):
        print(s)