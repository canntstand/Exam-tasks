for x in range(0, 22):
    nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n1 = f"27{nums[x]}98876"
    n2 = f"26{nums[x]}51"
    n3 = f"711{nums[x]}5"
    eq = int(n1, 22) + int(n2, 22) + int(n3, 22)

    if eq % 21 == 0:
        print(eq // 21)
        break
