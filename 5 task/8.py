def to_12(n):
    n12 = ""
    nums = "0123456789AB"
    
    while n > 0:
        n12 += nums[n % 12]
        n = n // 12
    
    return n12[::-1]

def f(n):
    nums = "0123456789AB"
    n12 = to_12(n)
    if n % 4 == 0:
        n12 = "2" + n12 + "64"
    else:
        nl = [nums.index(i) for i in n12]
        n12 += nums[max(nl)]
    return int(n12, 12)

ans = []

for n in range(1, 1000):
    r = f(n)
    if r > 1799:
        ans.append(r)

print(min(ans))