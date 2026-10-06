def f(s, e):
    if e == s: return 1
    if s > e: return 0
    
    st = str(s)
    
    if "1" in st:
        st = st.replace("1", "3")
        return f(s + 1, e) + f(int(st), e)
    
    return f(s + 1, e)

print(f(11, 94))