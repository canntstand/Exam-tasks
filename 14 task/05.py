def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

ans=0
for x in range(1,2301):
    if to_base(7350+7150-x,7).count('0')==200:
        ans=x
print(ans)
