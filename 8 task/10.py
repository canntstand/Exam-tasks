from itertools import product

letters = "АКОРСТ"
answer = 0
for i, word in enumerate(product(letters, repeat=5), 1):
    word = "".join(word)
    if i % 2 == 0 and word[0] not in "АСТ" and word.count("О") == 2:
        answer = i
print(answer)
