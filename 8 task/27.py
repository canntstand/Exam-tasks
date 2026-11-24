from itertools import combinations
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = set("aeiou")

valid_sets = sum(
    1
    for comb in combinations(alphabet, 10)
    if sum(1 for ch in comb if ch in vowels) >= 2
)

total = valid_sets * math.factorial(10)
print(total)
