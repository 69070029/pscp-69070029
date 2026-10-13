"""CuteCat CuteFox"""
total = int(input())
animal = {}

for _ in range(total):
    item = eval(input())
    animal.update(item)

print(animal.count("Cat"))