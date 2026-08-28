from itertools import permutations

answer = 0
for word in set(permutations("ЭКЗАМЕН")):
    if word[0] not in "ЭАЕ" and word[-1] in "ЭАЕ":
        answer += 1
print(answer)
