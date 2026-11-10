for x in range(0, 24):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = symbols[x]
    summ = sum(
        map(
            lambda y: int(y, 24),
            [f"4M{x}F", f"265AFDN{x}", f"N4{x}931B3L", f"NG{x}4F", f"FKJB5{x}IK"],
        )
    )

    if summ % 23 == 0:
        print(summ // 23)
