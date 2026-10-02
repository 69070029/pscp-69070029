"""yooob"""
text = input()

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        text[i] = text[i].replace(text[i], "")

print(text)