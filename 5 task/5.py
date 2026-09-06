def f(n):
    n2 = bin(n)[2:]
    sn2 = sum(map(int, list(n2)))
    if sn2 % 2 == 0:
        n2 += "0"
        n2 = "10" + n2[2:]
    else:
        n2 += "1"
        n2 = "11" + n2[2:]
    return int(n2, 2)

for n in range(1, 1000):
    r = f(n)
    if r <= 19:
        print(n)