for x in range(0, 22):
    nums = "0123456789ABCDEFGHIJKL"
    ans = int(f"12313{nums[x]}57", 22) + int(f"1{nums[x]}34561", 22)
    
    if ans % 21 == 0:
        print(nums[x], ans // 21)