def to_base(n,b):
    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s=''
    while n:
        s=d[n%b]+s
        n//=b
    return s

n=5*12**962021-4*2**162022+3*3**62023-2*6**2024-2025
s=to_base(n,36)
print(sum(c in '02468ACEGIKMOQSUWY' for c in s))
