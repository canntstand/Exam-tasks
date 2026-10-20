print("x y z w F")

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                eq = (w or x or not z or y) and (w or x or not z or not y) and (w or not x or not z or not y)
                if eq == 0:
                    print(x, y, z, w, int(eq))