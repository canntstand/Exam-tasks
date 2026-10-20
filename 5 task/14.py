def f(n):
    nb = bin(n)[2:]

    for _ in range(2):
        if nb.count("1") % 2 == 0:
            nb += "0"
        else:
            nb += "1"

    return int(nb, 2)


ans = []

for n in range(1, 1000):
    r = f(n)
    if r > 204:
        ans.append(r)

print(min(ans))
