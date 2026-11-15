ans = 0

for A in range(1, 128):
    if all(
        not (
            (((x & 49) != 0) <= (((x & A) != 0) <= ((x & 108) != 0)))
            <= (((x & 92) == 0) and ((x & A) != 0) and ((x & 49) != 0))
        )
        for x in range(1000)
    ):
        print(A)
