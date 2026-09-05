def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

n=7*512**120-6*64**100+8**210-255
print(to_base(n,8).count('0'))
