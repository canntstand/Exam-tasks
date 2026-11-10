f = open("17 task/17.txt")

l = [int(i) for i in f]
max_num = -1000000000
global_cnt = 0
max_sum = -1000000000

for i in l:
    if len(str(i)) == 4 and str(i)[-2:] == "42" and i > max_num:
        max_num = i

for i in range(len(l)):
    cnt_suitable_nums = 0
    if i + 2 < len(l):
        nums = [l[i], l[i + 1], l[i + 2]]
        for j in nums:
            j = str(abs(j))
            if len(j) == 4 and j[-2:] == "42":
                cnt_suitable_nums += 1

        if cnt_suitable_nums >= 2 and sum(nums) > max_num:
            global_cnt += 1

            if sum(nums) > max_sum:
                max_sum = sum(nums)

print(global_cnt, max_sum)