f = open("9 task/9.txt")
cnt = 0

for i in f:
    i = list(map(int, i.split()))
    nums_that_do_not_repeat = []
    max_and_min = [max(i), min(i)]
    already_checked = []
    repeats_2_times = 0
    not_max_not_min = False

    for j in i:
        if i.count(j) == 2 and j not in already_checked:
            repeats_2_times += 1
            already_checked.append(j)
        elif i.count(j) == 1:
            nums_that_do_not_repeat.append(j)

    for j in nums_that_do_not_repeat:
        if j not in max_and_min:
            not_max_not_min = True
            break

    if repeats_2_times >= 3 and not_max_not_min == True: # возможно repeats_2_times == 3, но ответ в обоих случаях и так одинаковый
        cnt += 1

print(cnt)
