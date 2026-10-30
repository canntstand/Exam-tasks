def f(k1, k2, x):
    if x == 3 and k1 + k2 >= 135:
        return True
    if x == 3 and k1 + k2 < 135:
        return False
    if k1 + k2 >= 135:
        return False

    return (
        f(k1 + 3, k2, x + 1)
        or f(k1 * 2, k2, x + 1)
        or f(k1, k2 + 3, x + 1)
        or f(k1, k2 * 2, x + 1)
    )


for S in range(1, 122):
    if f(13, S, 1):
        print(S)
