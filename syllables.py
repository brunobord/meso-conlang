"""
syllables
"""
from itertools import product
from random import choices, sample

consonants = ("p", "t", "k", "f", "s", "sh", "l", "w", "j", "m", "n")
vowels = ("a", "e", "i", "o", "u")

syllables = ["".join(x) for x in product(consonants, vowels)]

k = 20
print(f"{k} words\n")
for nb_syllables_list in sample((1, 2, 3, 4), k=k, counts=[10, 500, 300, 100]):
    picks = choices(syllables, k=nb_syllables_list)
    print(f"* {''.join(picks)}")
print()
