def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

for x in range(1,3001):
    if to_base(9150+930-x,9).count('0')==122:
        print(x)
        break
