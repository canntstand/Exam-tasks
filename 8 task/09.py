from itertools import product

letters = "ЕИОРТЯ"
answer = 0
for i, word in enumerate(product(letters, repeat=6), 1):
    word = "".join(word)
    if i % 2 == 1 and word[0] not in "РТЯ" and word.count("И") >= 2:
        answer = i
print(answer)
