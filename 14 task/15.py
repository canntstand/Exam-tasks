def to_11(x):
    x11 = ""
    nums = "0123456789AB"

    while x > 0:
        x11 += nums[x % 11]
        x //= 11
    return x11[::-1]


maxx = 0

for x in range(0, 3001):
    eq = to_11(9 * (11**210) + 8 * (11**150) - x)
    if eq.count("0") == 60 and x > maxx:
        print(eq)
        maxx = x

print(maxx)
