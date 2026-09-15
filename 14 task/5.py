def to_12(n):
    n12 = ""
    nums = "0123456789ABC"

    while n > 0:
        n12 += nums[n % 12]
        n //= 12

    return n12[::-1]

cnt = 0

for x in range(1, 3501):
    n = 12**457 + 12**48 - x
    n12 = to_12(n)
    if n12.count("0") > cnt:
        cnt = n12.count("0")

for x in range(1, 3501):
    n = 12**457 + 12**48 - x
    n12 = to_12(n)
    if n12.count("0") == cnt:
        print(x)
        break
