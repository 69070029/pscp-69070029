"""แถมๆ"""
def main():
    """input"""
    price = float(input())
    cap = int(input())
    trade = int(input())
    cus_money = float(input())

    daitaorai = int(cus_money // price)

    captaorai = 0
    taamtaorai = 0

    if not cap:
        pay = daitaorai
    else:
        for _ in range(daitaorai):
            if not captaorai % cap:
                taamtaorai += trade
                captaorai += trade
            captaorai += 1

        pay = taamtaorai + daitaorai

    print(pay)

main()
