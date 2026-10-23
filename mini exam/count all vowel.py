"""count all vowel"""

taorai = int(input())
count = 0
box = []

for _ in range(taorai):
    alpha = input()

    if alpha in "AEIOU":
        count += 1
        box.append(alpha)

print(count)

if "A" in box and "E" in box and "I" in box and "O" in box and "U" in box:
    print("YES")
else:
    print("NO")
