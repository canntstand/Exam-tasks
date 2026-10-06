def f(n):
    nb = bin(n)[2:]
    if n % 5 == 0:
        nb += nb[-3:]
    else:
        nb = bin((n % 5) * 5)[2:] + nb
    
    return int(nb, 2)

ans = []

for n in range(11, 1000):
    r = f(n)
    if r > 512:
        ans.append(n)

print(min(ans))