"""goods stock"""
goods = []
count = []

while True:
    rubna = input().split()
    command = rubna[0]

    if command == "END":
        break

    if command == "ADD":
        item = rubna[1]
        amount = int(rubna[2])

        if item in goods:
            count[goods.index(item)] += amount
        else:
            goods.append(item)
            count.append(amount)
    elif command == "REMOVE":
        item = rubna[1]
        amount = int(rubna[2])

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

    elif command == "CHECK":
        low_stock = [
            item for item, amount in zip(goods, count)
            if amount < 5
        ]

        if low_stock:
            print(*sorted(low_stock), sep="\n")
        else:
            print("All stocks are sufficient")

    elif command == "REPORT":
        for item, amount in sorted(zip(goods, count), reverse=True):
            print(f"{item}: {amount}")
