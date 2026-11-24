from itertools import combinations, permutations

word = "ХОЧУНАБЮДЖЕТ"
vowels = "ОУАЮЕ"
consonants = "ХЧНБДЖТ"

n = len(word)
v_count = len(vowels)

valid_v_positions = [
    pos for pos in combinations(range(n), v_count) if pos[-1] - pos[0] > 4
]

vowel_arrangements = sum(1 for _ in permutations(vowels))
consonant_arrangements = sum(1 for _ in permutations(consonants))

total = len(valid_v_positions) * vowel_arrangements * consonant_arrangements
print(total)
