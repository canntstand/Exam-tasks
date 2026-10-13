def f(n):
    nb = bin(n)[2:]
    nb += str(sum(map(int, nb)) % 2)
    nb += str(sum(map(int, nb)) % 2)
    return int(nb, 2)


ans = []

for n in range(1, 1000):
    r = f(n)
    if r < 86:
        ans.append(n)

print(max(ans))
