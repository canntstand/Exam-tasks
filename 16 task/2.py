F = [0] * 6251

for n in range(0, 6251):
    if n < 10:
        F[n] = n
    elif n >= 10:
        F[n] = 3 * n + F[n - 3]

print((F[6250] + 2 * F[6244]) / F[6238])
print((F[6250] + 2 * F[6244]) // F[6238])