def to_7(n):
    n7 = ""
    while n > 0:
        n7 += str(n % 7)
        n //= 7
    return n7[::-1]

def f(n):
    n7 = list(to_7(n))
    
    for i in range(len(n7)):
        num = int(n7[i])
        if num % 2 != 0:
            num += 1
        n7[i] = str(num)
    
    summ = sum(map(int, n7))
    
    n7 = list(to_7(summ)) + n7
    n7 = "".join(n7)
    
    if int(n7[0]) % 2 != 0:
        n7 = n7[0] + n7
    return int(n7, 7)
    
ans = []

for n in range(1, 2000):
    r = f(n)
    if r > 2000:
        ans.append(r)

print(min(ans))