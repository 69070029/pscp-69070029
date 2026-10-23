"""sorry"""
buy = []

while True:
    want = input()

    if want == "Sorry":
        buy.pop(-1)
        continue
    if want == "End":
        break

    buy.append(want)

print(*buy, sep=", ")
