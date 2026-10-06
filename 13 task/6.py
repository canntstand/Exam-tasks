def f(s, e):
    if s == e: return 1
    if s > e: return 0
    
    st = str(s)
    
    if st[1] < st[2]:
        st = st[0] + st[2] + st[1]
        
        return f(s + 1, e) + f(int(st), e)
    
    return f(s + 1, e)

print(f(101, 152))