"""CuteCat CuteFox"""
import ast

total = int(input())
animal = {}

for _ in range(total):
    catfox = ast.literal_eval(input())

    for name, num in catfox.items():
        animal[num.strip()] = name.strip()

if "Fubuki" not in animal.values() and "Fox01" not in animal:
    animal["Fox01"] = "Fubuki"

if "Garfield" not in animal.values() and "Cat01" not in animal:
    animal["Cat01"] = "Garfield"

def kk(x):
    """riang num"""
    return int(x[3:])

cat = sorted((c for c in animal if c.startswith("Cat")), key=kk)
fox = sorted((f for f in animal if f.startswith("Fox")), key=kk)

print(f"Cat : {len(cat)}")
print(f"Fox : {len(fox)}")

for a in cat + fox:
    print(f"{animal[a]} : {a}")
