"""Pad Thai"""
ingred = {"Pad Thai Sauce", "Tofu", "Pickle Turnip",
              "Shrimp", "Bean Sprouts", "Noodle", "Chives",
              "Lime", "Egg", "Oil", "Peanuts"}

while True:
    order = input()

    if order == "Cook":
        break

    if order not in ingred:
        print("This is not Pad Thai!!!")


    