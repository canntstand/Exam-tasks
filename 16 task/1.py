N = 7555447
F = [0] * N

for n in range(1, N):
    F.append(0)
    if n == 1:
        F[n] = 2
    elif n > 1 and F[n - 1] < 7555444:
        F[n] = F[n - 1] + 6
    else:
        F[n] = F[n - 1] - 7555444

print(F[7555446])
