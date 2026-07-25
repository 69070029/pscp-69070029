"""รหัสเซฟ"""
char = input()
digit = int(input())
if char == "H" and digit == 4567:
    print("safe unlocked")
elif char == "H" and digit != 4567:
    print("safe locked - change digit")
elif digit == 4567 and char != "H":
    print("safe locked - change char")
elif char != "H" and digit != 4567:
    print("safe locked")
