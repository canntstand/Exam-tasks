from sys import setrecursionlimit
from functools import lru_cache
from math import factorial

setrecursionlimit(5000)


@lru_cache(None)
def f(n):
    if n >= 1000:
        return factorial(n)
    if n < 1000 and n % 2 == 0:
        return f(n + 1) * n // 2
    if n < 1000 and n % 2 != 0:
        return f(n + 2) * n


print(f(18) / f(20))
