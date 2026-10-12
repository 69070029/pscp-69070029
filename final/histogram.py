"""Easy HIstogram no Dict"""
text = input()
box = []

for word in text:
    if word.isalpha() and not word in box:
        box.append(word)

def lekyai(x):
    """lekyaimakmak"""
    return (x.lower(), x.isupper())

for letter in sorted(box, key=lekyai):
    print(f"{letter} = {text.count(letter)}")
