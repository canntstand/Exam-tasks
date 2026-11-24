from itertools import *

s = "АПЕЛЬСИН"
consonants = "ПЛСН"
cnt = 0

for i in product(s, repeat=7):
    i = "".join(i)

    if "Ь" in i:
        if (
            len(set(i)) == len(i)
            and i.count("Ь") > 0
            and i.index("Ь") not in (0, 6)
            and i[i.index("Ь") - 1] in consonants
            and i[i.index("Ь") + 1] in consonants
        ):
            cnt += 1
    elif len(set(i)) == len(i):
        cnt += 1

print(cnt)
