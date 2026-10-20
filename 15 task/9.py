def Del(n, m):
    return n % m == 0

for A in range(101, 1000):
    if all([((Del(x, A) and Del(x, 36)) <= Del(x, 324)) for x in range(1, 10000)]):
        print(A)
        break