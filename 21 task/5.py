def f(k, x):
    if k <= 1:
        return x == 3 or x == 5

    if x > 4:
        return False

    if x % 2 != 0:
        return (
            f(k - 1, x + 1)
            and f(k - 4, x + 1)
            and f(k // 3, x + 1)
        )
    else:
        return (
            f(k - 1, x + 1)
            or f(k - 4, x + 1)
            or f(k // 3, x + 1)
        )


for s in range(4, 101):
    if f(s, 1):
        print(s)