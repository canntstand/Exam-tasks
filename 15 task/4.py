P = [i / 2 for i in range(19 * 2, 143 * 2)][:-1]
Q = [i / 2 for i in range(75 * 2, 186 * 2)][:-1]
A = []

for x2 in range(1 * 2, 1000 * 2):
    x = x2 / 2

    eq1 = x in Q
    eq2 = (not (x in A)) and (x in P)
    eq3 = not (x in Q)
    expr = not (eq1 <= (eq2 <= eq3))

    if expr == True:
        A.append(x)

print(max(A) - min(A))
