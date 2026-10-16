"""hamming"""
word1 = input()
word2 = input()

diff = 0

for a, b in zip(word1, word2):
    if a != b:
        diff += 1

print(diff)
