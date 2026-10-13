f = {}

for n in range(1, 101):
    f[n] = n ** n

f[1019] = 1 

for n in range(1018, 100, -1):
    f[n] = (n - 3) * (n // 508) * f[n + 1]

result = f[1016] / f[1017]
print(result)