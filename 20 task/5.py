def f(k, x):
    if x == 4 and k <= 1:
        return True
    if x != 4 and k <= 1:
        return False
    if x == 4 and k > 1:
        return False

    if x % 2 == 0:
        return f(k - 1, x + 1) and f(k - 4, x + 1) and f(k // 3, x + 1)
    else:
        return f(k - 1, x + 1) or f(k - 4, x + 1) or f(k // 3, x + 1)


for s in range(4, 101):
    if f(s, 1):
        print(s)
