for A in range(1, 1000):
    if all(
        [
            ((3 * y - x) > 12) or ((2 * x + 6 * y) >= 72) or (x > 24) or ((x * y) < A)
            for x in range(1, 400)
            for y in range(1, 400)
        ]
    ):
        print(A)
        break
