"""count vowels"""

WORD = input()

vowels = ["a", "e", "i", "o", "u"]
v = 0

for i in WORD:
    if i in vowels:
        v += 1

print(v)
