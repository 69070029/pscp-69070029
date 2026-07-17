"""ซื้อของ"""
def main():
    """input"""
    to_buy_list = input().split()

    carrot = 10 * int(to_buy_list[0])
    galumplee = 25 * int(to_buy_list[1])
    tomato = 3 * int(to_buy_list[2])

    total = carrot + galumplee + tomato
    print(total)

main()
