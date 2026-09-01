"""คำนวณราคาสินค้าโปรโมชั่น"""
def main():
    """input"""
    amount = list(map(int, input().split()))

    pay = (25 * amount[0]) + (40 * amount[1]) + (55 * amount[2])

    if amount[0] + amount[1] + amount[2] >= 3:
        pay = 0.9 * pay

    print(int(pay))

main()
