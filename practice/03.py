"""rahuspan"""
text = input()

upper = 0
lower = 0
digit = 0

for word in text:
    if word.isupper():
        upper += 1
    elif word.islower():
        lower += 1
    elif word.isdigit():
        digit += 1

if not upper or not lower or not digit or len(text) < 8:
    print("INVALID")
else:
    print("VALID")
