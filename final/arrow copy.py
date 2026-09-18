"""arrow"""
RL = input()
size = int(input())

middle = size - 1
total = size * 2 - 1

dokjun = []
wenwang = []

for i in range(1, size + 1):
    dokjun.append("*" * i)
for j in range(wenwang):
    wenwang.append(" " * j)

for word in RL:
    if word == "R":
        for i in range()