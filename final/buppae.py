"""rabbit buppae"""
rabbit1 = input()
rabbit2 = input()

name1 = list(rabbit1)
name2 = list(rabbit2)

if len(name1) > len(name2):
    for i in range(len(name1) - len(name2)):
        name2.append(name2[i])
elif len(name2) > len(name1):
    for j in range(len(name2) - len(name1)):
        name1.append(name1[j])

love = ['l', 'o', 'v', 'e']
new = []

for a, b in zip(name1, name2):
    if a.lower() in love or b.lower() in love:
        new.append("w")
    else:
        new.append("$")

count_w = 0
max_count_w = 0

for num in new:
    if num == "w":
        count_w += 1
        max_count_w = max(max_count_w, count_w)
    else:
        count_w = 0

if new.count("w") % 2:
    new.append(max_count_w)
else:
    if max_count_w < 2:
        new.append("#")

print(*new, sep="")
