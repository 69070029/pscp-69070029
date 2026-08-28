"""BASIC ATM"""
def main():
    """input"""
    money = int(input())

    if not 100 <= money <= 20000 or (money % 100):
        print("ERROR")
    else:
        while money >= 100:
            if money >= 1000:
                grey += money // 1000
                money = money % 1000
                print(f"1000 = {grey}")
            elif money >= 500:
                purple += money // 500
                money = money % 500
                print(f"500 = {purple}")
            elif money >= 100:
                red += money // 100
                money = money % 100
                print(f"100 = {red}")

main()
