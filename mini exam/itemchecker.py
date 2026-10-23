"""Item checker"""
mee = list(input().split())
check = input()

have = False

for word in mee:
    if word.lower() == check.lower():
        have = True
        break

if have:
    print(check, "is in the list")
else:
    print(check, "is not in the list")
