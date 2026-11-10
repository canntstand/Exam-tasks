from math import factorial

s = "ХОЧУНАБЮДЖЕТ"
vowels = "ОУАЮЕ"
consonants = "ХЧНБДЖТ"
n = factorial(len(s))
n_forbidden = factorial(len(consonants) + 1) * factorial(len(vowels))
print(n - n_forbidden)
