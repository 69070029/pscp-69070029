"""แถมๆ"""
def main():
    """input"""
    price = float(input())
    cap = int(input())
    trade = int(input())
    cus_money = float(input())

    daitaorai = int(cus_money // price)

    if not cap:
        total = daitaorai
    else:
        total = daitaorai
        captaorai = daitaorai

        while captaorai >= cap:
            taamtaorai = (captaorai // cap) * trade
            total += taamtaorai
            captaorai = (captaorai % cap) + taamtaorai

    print(total)

main()
