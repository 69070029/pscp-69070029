"""bus seat"""
col = int(input())
row = int(input())
seat = int(input())

for i in range(col):
    bus = [(col * (j + 1) - i) for j in range(row)]

    for j in range(row):
        if len(str(bus[j])) == 1:
            bus[j] = "0" + str(bus[j])
        if int(bus[j]) == seat:
            bus[j] = "XX"

    print(*bus)
    if i % 2 and i != col - 1:
        print()
