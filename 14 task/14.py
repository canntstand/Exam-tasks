l = []

for x in "0123456789abc":
    s1 = f"537{x}623"
    s2 = f"6{x}35{x}2"

    if (int(s1, 13) - int(s2, 13)) % 3 == 0:
        l.append(x)

print(max(map(lambda x: int(x, 13), l)))
