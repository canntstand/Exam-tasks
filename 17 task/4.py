f = open("17 task/17.txt")
l = [int(i) for i in f]
ans = []
cnt = 0
max_43 = 0

for i in sorted(l)[::-1]:
    if str(i)[-2:] == "43":
        max_43 = i
        break

for i in range(len(l)):
    if i + 2 < len(l):
        nums = sorted([l[i], l[i + 1], l[i + 2]])
        av = sum(nums) / 3

        if av > 0 and av < max_43 and any(1000 <= abs(x) <= 9999 for x in nums):
            ans.append(sum(nums))
            cnt += 1


print(cnt, max(ans))
