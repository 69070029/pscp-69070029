"""Pad Thai"""
saiarai = set()
rosarai = set()

ingred = {"Pad Thai Sauce", "Tofu", "Pickle Turnip",
            "Shrimp", "Bean Sprouts", "Noodle", "Chives",
            "Lime", "Egg", "Oil", "Peanuts"}

flavor = {"Sweet", "Sour", "Salty"}

while True:
    order = input()

    if order == "Cook":
        break
    saiarai.add(order)

while True:
    taste = input()

    if taste == "End":
        break
    rosarai.add(taste)

if rosarai == flavor and saiarai == ingred:
    print("Delicious!")
elif any(x not in ingred for x in saiarai):
    print("This is not Pad Thai!!!")
elif len(saiarai) < len(ingred):
    print("This is bad!")
else:
    print("Not Bad...")
