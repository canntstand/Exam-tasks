for A in range(1, 500):
    ans = []
    for x in range(1, 2000):
        Q = x % 3 == 0
        P = x % 5 == 0

        A_cond = x % A == 0

        expr = Q <= (P <= (Q and A_cond))

        if not expr:
            ans.append(False)
        else:
            ans.append(True)
    if all(ans):
        print(A)
