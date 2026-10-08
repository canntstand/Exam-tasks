P = [i / 2 for i in range(15 * 2, 41 * 2)][:-1]
Q = [i / 2 for i in range(21 * 2, 64 * 2)][:-1]
A = []


def eq(x):
    eq1 = not (x in P)
    eq2 = (x in Q) and not (x in A)
    eq3 = x in P
    eq_final = eq1 <= (eq2 <= eq3)

    return eq_final


for x in range(1 * 2, 10000 * 2):
    x = x / 2
    if not eq(x):
        A.append(x)

print(A)
from math import floor, ceil
print(ceil(max(A)) - floor(min(A)))
