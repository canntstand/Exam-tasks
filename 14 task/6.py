def to_36(n):
    nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n36 = ""
    while n > 0:
        n36 += str(nums[n % 36])
        n //= 36
    
    return n36

n = (5 * (7776 ** 7)) + (4 * (1296 ** 6)) + 3 * 216 - 7776
n36 = to_36(n)
print(n36.count("I") + n36.count("U") + n36.count("Z"))
