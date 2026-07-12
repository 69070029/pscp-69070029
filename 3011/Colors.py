"""COLORS"""
color1 = str(input())
color2 = str(input())

if color1 == "Red" and color2 == "Yellow" or color1 == "Yellow" and color2 == "Red":
    print("Orange")
elif color1 == "Red" and color2 == "Blue" or color1 == "Blue" and color2 == "Red":
    print("Violet")
elif color1 == "Yellow" and color2 == "Blue" or color1 == "Blue" and color2 == "Yellow":
    print("Green")
else:
    print("Error")