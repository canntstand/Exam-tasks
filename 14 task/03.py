def value(s,b):
    d={str(i):i for i in range(10)}
    d.update({chr(55+i):i for i in range(10,36)})
    n=0
    for c in s:
        n=n*b+d[c]
    return n

digits='0123456789ABCDEFGHIJKLMNOPQ'
ans=0
for x in range(27):
    c=digits[x]
    n=value('KLMN'+c+'1227',27)+value('F'+c+'GHI3427',27)
    if n%26==0:
        ans=max(ans,n//26)
print(ans)
