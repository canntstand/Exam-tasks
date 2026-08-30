def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

for x in range(1,2031):
    if to_base(6260+6160+660-x,6).count('0')==202:
        print(x)
        break
