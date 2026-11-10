def f(n):
    nb = bin(n)[2:]
    if n % 3 == 0:
        nb += nb[-2:]
    else:
        nb += bin((n % 3) * 3)[2:]
    
    return int(nb, 2)

ans = []

for n in range(1, 1000):
    r = f(n)
    if r >= 195:
        ans.append(r)

print(min(ans))