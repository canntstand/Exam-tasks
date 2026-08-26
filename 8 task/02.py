from itertools import product

letters = "АЕЛПРЬ"
answer = 0
for i, word in enumerate(product(letters, repeat=5), 1):
    word = "".join(word)
    if i % 2 == 0 and word[0] not in "ЬР" and word.count("Л") >= 2:
        answer = i
print(answer)
