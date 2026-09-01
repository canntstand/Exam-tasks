def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

ans=0
for x in range(1,2031):
    if to_base(3100-x,3).count('0')==5:
        ans=x
print(ans)
