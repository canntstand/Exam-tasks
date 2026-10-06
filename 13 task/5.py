def f(s, e):
    if s == e:
        return 1
    if s < e:
        return 0
    if s == 15:
        return 0

    return f(s - 2, e) + f(s - 3, e) + f(s // 2, e)


print(f(33, 22) * f(22, 4))
