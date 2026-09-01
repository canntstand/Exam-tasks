from itertools import product

answer = 0
for word in product("0123456", repeat=5):
    if word[0] != "0" and word.count("6") == 1 and all(word[i] != word[i + 1] for i in range(4)):
        answer += 1
print(answer)
