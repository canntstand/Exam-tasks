def to_3(n):
    n3 = ""
    
    while n > 0:
        n3 += str(n % 3)
        n //= 3
    
    return n3[::-1]

def f(n):
    n3 = to_3(n)
    n3 = sorted(n3)[::-1]
    n3.append(n3[0])
    return int("".join(n3), 3)

ans = []

for n in range(1, 1000):
    r = f(n)
    if r < 1200:
        ans.append(r)

print(max(ans))