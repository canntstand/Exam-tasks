def f(n):
    l = "0123456789abcdef"
    nb = list(hex(n)[2:])

    for n in range(len(nb)):
        if nb[n] != "f":
            nb[n] = l[l.index(nb[n]) + 1]

    n = sum(map(int, str(int("".join(nb[::-1]), 16))))

    return n


for n in range(100, 1000):
    if f(n) == 12:
        print(n)
        break
