"""classify"""
name = []

while True:
    rahus = input()

    if rahus == "END":
        break

    name.append(rahus)

name = sorted(name)

year = sorted(list(set(x[:2] for x in name)))

for yr in year:
    faculty = sorted(list(set(x[2:4] for x in name if x[:2] == yr)))
    current = 0

    for num in faculty:
        if not current:
            print(f"{yr} {int(num)} {sum(1 for x in name if x[:2] == yr and x[2:4] == num)}")
        else:
            print(f"-- {int(num)} {sum(1 for x in name if x[:2] == yr and x[2:4] == num)}")

        current += 1
