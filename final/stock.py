"""goods stock"""
goods = []
count = []
while True:
    rubna = input()

    if rubna == "END":
        break

    if rubna.startswith("ADD"):
        item = rubna.split()[1]
        amount = int(rubna.split()[2])

        if item in goods:
            count[goods.index(item)] += amount
        else:
            goods.append(item)
            count.append(amount)

    elif rubna.startswith("REMOVE"):
        item = rubna.split()[1]
        amount = int(rubna.split()[2])

        if item not in goods:
            goods.append(item)
            count.append(0)
            print(f"Not enough stock for {item}")
        else:
            idx = goods.index(item)
            if count[idx] >= amount:
                count[idx] -= amount
            else:
                count[idx] = 0
                print(f"Not enough stock for {item}")

    elif rubna == "REPORT":
        result = sorted(zip(count, goods), reverse=True)

        for i, a in result:
            print(f"{a}: {i}")

    else:
        lessthan5 = []
        for stuff in count:
            if stuff < 5:
                lessthan5.append(item)
        if len(lessthan5) < 1:
            print("All stocks are sufficient")
        else:
            for item in sorted(lessthan5):
                print(item)
