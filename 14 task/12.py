def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

s=to_base(2*729**75+2*243**78+8181+2*2784+2*987+58,27)
print(s[1:].count('0'))
