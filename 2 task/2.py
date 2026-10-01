print("x y z w F")

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                eq = (x and (not y)) or (y == z) or (not w)
                if eq == 0:
                    print(x, y, z, w, int(eq))
