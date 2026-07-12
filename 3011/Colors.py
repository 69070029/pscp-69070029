"""COLORS"""
Color1 = str(input())
Color2 = str(input())

if Color1 == "Red" and Color2 == "Yellow" or Color1 == "Yellow" and Color2 == "Red":
    print("Orange")
elif Color1 == "Red" and Color2 == "Blue" or Color1 == "Blue" and Color2 == "Red":
    print("Violet")
elif Color1 == "Yellow" and Color2 == "Blue" or Color1 == "Blue" and Color2 == "Yellow":
    print("Green")
else:
    print("Error")
