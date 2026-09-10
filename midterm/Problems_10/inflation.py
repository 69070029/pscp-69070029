"""inflation"""
def main():
    """input"""
    price = float(input())
    year = int(input())

    price = int(price * 100)

    for _ in range(year):
        price += (price * 381) // 10000

    print(f"{price // 100}.{price % 100:02d}")
main()
