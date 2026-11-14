def f(l, x):
    l = sorted(l)
    
    if l[0] == l[1] and (x == 5 or x == 3): return True
    if l[0] != l[1] and x == 5: return False
    if l[0] == l[1] and x != 5: return False
    
    if x % 2 == 1:
        return f([l[0] + 1, l[1]], x + 1) and f([l[0] + 3, l[1]], x + 1)
    else:
        return f([l[0] + 1, l[1]], x + 1) or f([l[0] + 3, l[1]], x + 1)
        

for s in range(1, 24):
    if f([13, s], 1):
        print(s)
        
        

### Доп

def check(s):
    l = sorted([13, s])

    for add in (1, 3):
        new_l = sorted([l[0] + add, l[1]])

        diff = new_l[1] - new_l[0]

        if diff in (1, 3):
            return True

    return False


for s in (5, 7, 19, 21):
    if check(s):
        print(s)