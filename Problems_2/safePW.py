"""ตู้เซฟ"""
def main():
    """ใส่รหัส"""
    letter = str(input())
    numbers = str(input())

    if letter == "H" and numbers == "4567":
        print("safe unlocked")
    elif letter != "H" and numbers == "4567":
        print("safe locked - change char")
    elif letter == "H" and numbers != "4567":
        print("safe locked - change digit")
    else:
        print("safe locked")

main()
