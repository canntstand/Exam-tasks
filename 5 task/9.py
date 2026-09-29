def f(n):
    n_bin = bin(n)[2:]
    if n % 3 == 0:
        n_bin += n_bin[-3:]
    else:
        rem = bin((n % 3) * 3)[2:]
        n_bin += rem
    
    return int(n_bin, 2)
        

ans = []
for n in range(1, 1000):
    r = f(n)
    if r <= 137:
        ans.append(r)

print(max(ans))
