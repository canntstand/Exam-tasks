def f(k1, k2, x):
    if x == 3 and k1 + k2 >= 133:
        return True
    if x == 3 and k1 + k2 < 133:
        return False
    if k1 + k2 >= 133:
        return False

    return (
        f(k1 + 4, k2, x + 1)
        or f(k1 * 2, k2, x + 1)
        or f(k1, k2 + 4, x + 1)
        or f(k1, k2 * 2, x + 1)
    )


for k2 in range(1, 116):
    if f(17, k2, 1):
        print(k2)
        break
