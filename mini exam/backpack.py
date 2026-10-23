"""backpack"""
bag = list(input().split(","))
found = input()

if "Empty" in bag:
    bag = []

if found == "Stone":
    print("I don't need this!")
else:
    if len(bag) == 5:
        bag.pop(0)

    bag.append(found)

print(bag)
