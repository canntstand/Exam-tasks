f = open("17 task/17.txt")
l = []
max_sum = 0
max_43_num = -100000000000000000000
cnt = 0

for i in f:
    i = int(i)
    l.append(i)

    if "43" == str(i)[-2:] and i > max_43_num:
        max_43_num = i

for i in range(len(l)):
    if i + 2 < len(l):
        nums = sorted([l[i], l[i + 1], l[i + 2]])
        summ = sum(nums)

        if (
            len(str(abs(nums[0]))) == 4
            or len(str(abs(nums[1]))) == 4
            or len(str(abs(nums[2]))) == 4
        ) and ((summ / 3) > 0 and (summ / 3) < max_43_num):
            cnt += 1

            if summ > max_sum:
                max_sum = summ

print(cnt, max_sum)
