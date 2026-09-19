def count_0(n):
    cnt = 0

    while n > 0:
        if n % 7 == 0:
            cnt += 1
        n //= 7

    return cnt


ans = 0

for x in range(1, 2031):
    eq = 7**170 + 7**100 - x
    hmz = count_0(eq)
    if hmz == 71 and x > ans:
        ans = x

print(ans)
