"""สถานะน้ำ"""
def main():
    """input"""
    temp = int(input())
    CF = input().lower()

    if CF == "c":
        if temp <= 0:
            print("solid")
        elif temp >= 100:
            print("gas")
        else:
            print("liquid")
    elif CF == "f":
        if temp <= 32:
            print("solid")
        elif temp >= 212:
            print("gas")
        else:
            print("liquid")

main()
