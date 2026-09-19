ans = []

for A in range(1, 100):
    if all(
        [
            ((x + y) <= 30) or (y <= (x + 2)) or (y >= A)
            for x in range(1, 1000)
            for y in range(1, 1000)
        ]
    ):
        ans.append(A)

print(max(ans))
