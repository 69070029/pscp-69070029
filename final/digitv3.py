"""digit v3"""
words = {
    "zero": 0,
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90
}

n = input().split()
total = 0
current = 0

for word in n:
    if word == "thousand":
        total += current * 1000
        current = 0
    elif word == "hundred":
        total += current * 100
        current = 0
    else:
        current += words[word]

print(total + current)
