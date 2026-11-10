from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(5000)

@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    else:
        return n * 2 + f(n + 2)


print(f(82) - f(81))
