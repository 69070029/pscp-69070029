"""COLORS"""
COLOR_1 = str(input())
COLOR_2 = str(input())

if COLOR_1 == "Red" and COLOR_2 == "Yellow" or COLOR_1 == "Yellow" and COLOR_2 == "Red":
    print("Orange")
elif COLOR_1 == "Red" and COLOR_2 == "Blue" or COLOR_1 == "Blue" and COLOR_2 == "Red":
    print("Violet")
elif COLOR_1 == "Yellow" and COLOR_2 == "Blue" or COLOR_1 == "Blue" and COLOR_2 == "Yellow":
    print("Green")
elif COLOR_1 == "Yellow" and COLOR_2 == "Yellow":
    print("Yellow")
elif COLOR_1 == "Blue" and COLOR_2 == "Blue":
    print("Blue")
elif COLOR_1 == "Red" and COLOR_2 == "Red":
    print("Red")
else:
    print("Error")
