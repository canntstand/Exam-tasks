def f(n):
    nb = bin(n)[2:]
    
    if n % 2 == 0:
        nb += "10"
    else:
        nb = "1" + nb + "01"
    
    return int(nb, 2)

for n in range(1000):
    if f(n) >= 190:
        print(n)
        break