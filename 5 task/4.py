def to_4(n):
    n4 = ""
    
    while n > 0:
        n4 += str(n % 4)
        n = n // 4
    
    return n4[::-1]

def f(n):
    n4 = to_4(n)
    if n % 4 == 0:
        n4 += (n4[-2] + n4[-1])
    else:
        n4_sum = sum(map(int, list(n4))) * 4
        n4 += to_4(n4_sum)
    
    return int(n4, 4)

ans = []

for n in range(1, 500):
    r = f(n)
    if r % 2 == 0 and r > 211 and r % 3 == 0:
        ans.append(r)

print(min(ans))