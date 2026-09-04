def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

n=7*49**120-6*343**65-5*7**40
print(to_base(n,7).count('6'))
