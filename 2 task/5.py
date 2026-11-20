print("x y z w F")

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = int(((y <= w) <= x) or not z)
                if f == 0:
                    print(x, y, z, w, f)