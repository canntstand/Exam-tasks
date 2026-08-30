from itertools import product

letters = "ГЕКЛО"
answer = 0
for i, word in enumerate(product(letters, repeat=6), 1):
    word = "".join(word)
    positions = [j for j, c in enumerate(word) if c == "Г"]
    if len(positions) >= 2 and any(positions[b] - positions[a] > 1 for a in range(len(positions)) for b in range(a + 1, len(positions))):
        answer = i
print(answer)
