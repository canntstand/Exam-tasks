def f(k, x):
    if k >= 124 and x == 3: return True
    if k < 124 and x == 3: return False
    if k >= 124 and x != 3: return False
    
    if x % 2 != 0:
        return f(k + 1, x + 1) and f(k + 5, x + 1) and f(k * 3, x + 1)
    
    return f(k + 1, x + 1) or f(k + 5, x + 1) or f(k * 3, x + 1)

for s in range(1, 124):
    if f(s, 1):
        print(s)
        break