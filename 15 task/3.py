B = [i / 2 for i in range(22 * 2, 41 * 2)][:-1]
C = [i / 2 for i in range(32 * 2, 51 * 2)][:-1]
A = []

while True:
    if all(
        [
            True
            if (not x / 2 in A) <= ((x / 2 in B) == (x / 2 in C))
            else A.append(x / 2)
            for x in range(1 * 2, 100 * 2)
        ]
    ):
        print(max(A) - min(A))
        break
