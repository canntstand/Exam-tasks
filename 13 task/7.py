ans = set()

def f(x, cnt):
    if cnt == 5:
        ans.add(x)
        return
    
    f(x + 4, cnt + 1)
    f(x * 2, cnt + 1)

f(2, 0)

print(len(ans))