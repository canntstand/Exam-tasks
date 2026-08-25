from itertools import product

letters = "АЕЛПРЬ"
for i, word in enumerate(product(letters, repeat=6), 1):
    word = "".join(word)
    if i % 2 == 1 and word[0] not in "АЛ" and word.count("П") >= 2:
        print(i)
        break
