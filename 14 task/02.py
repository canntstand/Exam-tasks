def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

ans=0
for x in range(1,2501):
    if to_base(585+57-x,5).count('0')==80:
        ans=x
print(ans)
