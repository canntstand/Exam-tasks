def to_5(n):
    n_5 = ""
    while n > 0:
        n_5 += str(n % 5)
        n = n // 5
    return n_5


def f(n):
    n_5 = to_5(n)
    return int(n_5, 5)


for n in range(1, 1000):
    num = f(n)
    if num == 61:
        print(n)
        break