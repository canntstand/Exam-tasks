def f(n):
    bn = bin(n)[2:]
    bni = map(int, list(bn))
    if sum(bni) % 2 == 0:
        bn += "00"
        bn = "11" + bn[2:]
    else:
        bn += "01"
        bn = "10" + bn[2:]
    
    return int(bn, 2)

for n in range(1, 1000):
    r = f(n)
    
    if r > 96:
        print(n)
        break