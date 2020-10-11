# s = 'azcbobobegghakl'

VOWELS = ('a', 'e', 'i', 'o', 'u')
num_vowels = 0

for c in s:
    if c in VOWELS:
        num_vowels += 1

print("Number of vowels:", num_vowels)
