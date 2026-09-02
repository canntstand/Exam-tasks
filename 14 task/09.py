def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

ans=0
for x in range(1,2043):
    if to_base(2561+5178-x,5).count('0')==60:
        ans=x
print(ans)
