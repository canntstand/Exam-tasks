from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(5000)


@lru_cache(None)
def f(n):
    if n >= 2024:
        return 1
    else:
        return f(n + 2) + f(n + 4)


n = 1
ans = set()

while n <= 2024:
    num = f(n)
    ans.add(num)
    n += 1

print(len(ans))
