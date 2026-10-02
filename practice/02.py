"""lek dod"""
num = input()
start = 1
count = 0

for word in num:
    if word != "0":
        start *= int(word)
        count += 1

if not count:
    print(0)
else: print(start)
