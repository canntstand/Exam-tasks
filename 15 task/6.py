P = [i for i in range(5, 41)]
Q = [i for i in range(2, 135) if 135 % i == 0]

ans = []

for y in range(1, 2000):
    A = [i for i in range(2, y) if y % i == 0]

    if len(A) > 0:
        if all(not (((x in P) <= (x in Q)) and (x in A)) for x in A):
            ans.append(y)

print(max(ans))
