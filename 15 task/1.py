def dell(n, m):
    return n % m == 0


b = [i for i in range(70, 91)]
ans = 0

for A in range(1, 1000):
    if (
        all([(dell(x, A) or ((x in b) <= (not dell(x, 22)))) for x in range(1, 1000)])
        and A > ans
    ):
        ans = A

print(ans)
