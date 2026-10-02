"""num tua aksorn"""
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

print(upper, lower, digit)
