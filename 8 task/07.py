from itertools import product

letters = "АГИЛМОРТ"
for i, word in enumerate(product(letters, repeat=5), 1):
    word = "".join(word)
    if i % 2 == 0 and word[0] not in "АГ" and word.count("Р") >= 2:
        print(i)
        break
