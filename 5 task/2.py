def to_4(n):
    n4 = ""
    
    while n > 0:
        n4 += str(n % 4)
        n = n // 4
    
    return n4[::-1]

def f(n):
    n4 = list(to_4(n))
    r = ""
    for i in n4:
        if i != "0":
            r += i
    return int(r, 4)

print(f(48))