def f(s, e):
    if s == e: return True
    if s < e: return False
    if s == 22: return False
    
    return f(s - 2, e) + f(s // 2, e) + f(s // 3, e)

print(f(40, 2))