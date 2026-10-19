"""horizon histogram"""
text = input()

for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in text:
        continue

    count = text.count(chr(i))

    ans = ""

    for j in range(count):
        ans += "-"
        if not (j + 1) % 5 and j != count - 1:
            ans += "|"

    print(f"{chr(i)} : {ans}")

for i in range(ord('A'), ord('Z') + 1):
    if chr(i) not in text:
        continue

    count = text.count(chr(i))

    ans = ""

    for j in range(count):
        ans += "-"
        if not (j + 1) % 5 and j != count - 1:
            ans += "|"

    print(f"{chr(i)} : {ans}")
