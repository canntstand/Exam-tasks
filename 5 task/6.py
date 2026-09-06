def to_3(n):
    n3 = ""

    while n > 0:
        n3 += str(n % 3)
        n = n // 3

    return n3[::-1]


def f(n):
    n3 = to_3(n)

    if n % 3 == 0:
        n3 += n3[-2] + n3[-1]
    else:
        rem = (n % 3) * 5
        rem3 = to_3(rem)
        n3 += rem3

    return int(n3, 3)


ans = []

for n in range(1, 500):
    r = f(n)
    if r > 150:
        ans.append(r)

print(min(ans))
