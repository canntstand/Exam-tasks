def value(s,b):
    d={str(i):i for i in range(10)}
    d.update({chr(55+i):i for i in range(10,36)})
    n=0
    for c in s:
        n=n*b+d[c]
    return n

digits='0123456789ABCDEFG'
ans=0
for x in range(17):
    c=digits[x]
    n=value('5432'+c+'6717',17)+value('302'+c+'17',17)
    if n%19==0:
        ans=max(ans,n)
print(ans)
