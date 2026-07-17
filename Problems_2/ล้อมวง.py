"""ล้อมรั้ว"""
def main():
    """input"""
    WLL = input().split()
    cost = int(input())

    total = ((int(WLL[0]) * 2) + (int(WLL[1]) * 2)) * int(WLL[2])
    price = cost * total

    print(total)
    print(price)

main()
