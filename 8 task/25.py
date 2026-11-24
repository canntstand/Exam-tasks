from itertools import *

s = "КЛАБХАУС"
cnt = 0

unique_words = {"".join(p) for p in permutations(s)}

for i in unique_words:
    if "АА" not in i:
        cnt += 1

print(cnt)