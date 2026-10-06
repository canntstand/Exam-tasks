ans = set()


def f(x, cnt):
    if cnt == 4:
        ans.add(x)
        return

    f(x + 2, cnt + 1)
    f(x * 3, cnt + 1)


f(1, 0)

print(len(ans))
