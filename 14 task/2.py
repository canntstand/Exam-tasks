def to_25(n):
    nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n25 = ""
    
    while n > 0:
        n25 += nums[n % 25]
        n //= 25
    
    return n25[::-1]

n = 3 * (3125 ** 8) + 2 * (625 ** 7) - 4 * (625 ** 6) + 3 * (125 ** 5) - 2 * (25 ** 4) - 2025
print(to_25(n).count("0"))