"""Pick Them"""
box = list(map(int, input().strip("[]").split(",")))
even = []

for num in box:
    if not num % 2:
        even.append(num)

if len(even) <= 0:
    print("Nope")
else: print(*even, sep="\n")
