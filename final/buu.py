"""BUU"""
text = input().upper()

if not "B" in text:
    new = "B"

    while len(new) < len(text):
        if new[-2:] == "UU":
            new += "B"
        else: new += "U" #BUUBUU...

    print(new)

elif not "BUU" in text:
    pos = text.index("B")
    print(text[:pos + 1] + "U" * (len(text) - pos - 1))

else:
    uu = []
    howmuch = 0

    for i, char in enumerate(text):
        if char == "B":
            j = i + 1

            while j < len(text) and text[j] == "U":
                howmuch += 1
                j += 1

        uu.append(howmuch)
        howmuch = 0

    count = max(uu)

    print("Yes", count)
