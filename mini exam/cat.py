"""cat in the bag"""
bag = []

while True:
    luggage = input()

    if luggage == "-1":
        break

    bag.append(luggage.lower())

cat_count = 0
cat = []

for thing in bag:
    if "cat" in thing.lower():
        cat_count += 1
        cat.append(thing)

print(f"The number of cat in bag {cat_count}")
print(f"List of cat {cat}")
