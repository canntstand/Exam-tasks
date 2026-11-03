def f(k1, k2, x, previous):
    if k1 + k2 <= 42 and (x == 5 or x == 3): return True 
    if k1 + k2 > 42 and x == 5: return False 
    if k1 + k2 <= 42: return False
    
    if previous == "k1-4":
        if x % 2 != 0:
            return f(k1 // 3, k2, x + 1, previous="k1//3") and f(k1, k2 - 4, x + 1, previous="k2-4") and f(k1, k2 // 3, x + 1, previous="k2//3")
        else:
            return f(k1 // 3, k2, x + 1, previous="k1//3") or f(k1, k2 - 4, x + 1, previous="k2-4") or f(k1, k2 // 3, x + 1, previous="k2//3")
    if previous == "k1//3":
        if x % 2 != 0:
            return f(k1 - 4, k2, x + 1, previous="k1-4") and f(k1, k2 - 4, x + 1, previous="k2-4") and f(k1, k2 // 3, x + 1, previous="k2//3")
        else:
            return f(k1 - 4, k2, x + 1, previous="k1-4") or f(k1, k2 - 4, x + 1, previous="k2-4") or f(k1, k2 // 3, x + 1, previous="k2//3")
    if previous == "k2-4":
        if x % 2 != 0:
            return f(k1 // 3, k2, x + 1, previous="k1//3") and f(k1, k2 // 3, x + 1, previous="k2//3") and f(k1 - 4, k2, x + 1, previous="k1-4")
        else:
            return f(k1 // 3, k2, x + 1, previous="k1//3") or f(k1, k2 // 3, x + 1, previous="k2//3") or f(k1 - 4, k2, x + 1, previous="k1-4")
    if previous == "k2//3":
        if x % 2 != 0:
            return f(k1 // 3, k2, x + 1, previous="k1//3") and f(k1 - 4, k2, x + 1, previous="k1-4") and f(k1, k2 - 4, x + 1, previous="k2-4")
        else:
            return f(k1 // 3, k2, x + 1, previous="k1//3") or f(k1 - 4, k2, x + 1, previous="k1-4") or f(k1, k2 - 4, x + 1, previous="k2-4")
    if previous == "":
        if x % 2 != 0:
            return f(k1 // 3, k2, x + 1, previous="k1//3") and f(k1 - 4, k2, x + 1, previous="k1-4") and f(k1, k2 - 4, x + 1, previous="k2-4") and f(k1, k2 // 3, x + 1, previous="k2//3")
        else:
            return f(k1 // 3, k2, x + 1, previous="k1//3") or f(k1 - 4, k2, x + 1, previous="k1-4") or f(k1, k2 - 4, x + 1, previous="k2-4") or f(k1, k2 // 3, x + 1, previous="k2//3")

ans = []

for s in range(1, 1000):
    if f(50, s, 1, previous=""):
        ans.append(s)

print(ans)
print(max(ans))