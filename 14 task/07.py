def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

ans=0
for x in range(1,2031):
    if to_base(791+7160-x,7).count('0')==70:
        ans=x
print(ans)
