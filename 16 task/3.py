F = [0] * (10 ** 6 + 1)
cnt = 0

for n in range(0, (10 ** 6) + 1):
    if n < 10:
        F[n] = n
    elif n >= 10 and n < 1000:
        F[n] = F[n // 10] + F[n % 10]
    elif n >= 1000:
        F[n] = F[n // 1000] - F[n % 1000]
        
    if F[n] == 0:
        cnt += 1

print(cnt)