"""เดินเล่น"""
char = input().upper()
x = 0
y = 0

for i in char:
    if i == "N":
        y += 1
    elif i == "S":
        y -= 1
    elif i == "E":
        x += 1
    else:
        x -= 1
print(f"{x} {y} {abs(x) + abs(y)}")
