def f(s, a):
    if s >= 100 or s in a:
        return
    
    a.add(s)
    f(s + 3, a)
    f(s * 3, a)
    
a = set()
f(10, a)
    
print(sum(x % 2 != 0 for x in a))