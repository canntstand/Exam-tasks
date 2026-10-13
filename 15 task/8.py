X = [i for i in range(1, 100) if i >= 22 and i <= 70 and i not in (26, 40)]
W = [i for i in range(1, 100) if i not in X]
F = [i for i in X if len(str(i)) == 2 and sum(map(int, str(i))) > 5]
M = []

for n in range(1, 1000):
    if not ((n not in W) <= ((n not in F) or (n in M))):
        M.append(n)

print(len(M))