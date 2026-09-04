from itertools import product

answer = 0
for word in product("БЛОГЕР", repeat=4):
    if word.count("Г") == 1 and all(not (word[i] in "ОЕ" and word[i + 1] in "ОЕ") for i in range(3)):
        answer += 1
print(answer)
