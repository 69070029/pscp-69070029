"""CuteCat CuteFox"""
total = int(input())
animal = {}

for _ in range(total):
    catfox = input()

    key, value = catfox.strip("{}").replace('"', '').split(" : ")
    animal[key] = value

if "Fubuki" not in animal and "Fox01" not in animal.values():
    animal["Fubuki"] = "Fox01"

if "Garfield" not in animal and "Cat01" not in animal.values():
    animal["Garfield"] = "Cat01"

print(f"Cat : {sum(value.startswith("C") for value in animal.values())}")
print(f"Fox : {sum(value.startswith("F") for value in animal.values())}")

def kk(x):
    """riang cat-fox 01-n"""
    return x[1][0], int(x[1][-2:])

animal = dict(sorted(animal.items(), key=kk))

for key, value in animal.items():
    print(f"{key} : {value}")
