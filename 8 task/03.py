from itertools import product

letters = "EINSVX"
target = "SIXSEVEN"
answer = 0
for word in product(letters, repeat=8):
    word = "".join(word)
    if word < target and sum(c in "EI" for c in word) == 2:
        answer += 1
print(answer)
