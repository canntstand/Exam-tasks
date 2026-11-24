from itertools import *

s = "НИЧЬЯ"
vowels = "ИЯ"
cnt = 0

for i in product(s, repeat=7):
    i = "".join(i)

    vowels_pos = [idx for idx, ch in enumerate(i) if ch in vowels]

    if len(vowels_pos) == 2 and abs(vowels_pos[0] - vowels_pos[1]) > 1:
        cnt += 1

print(cnt)
