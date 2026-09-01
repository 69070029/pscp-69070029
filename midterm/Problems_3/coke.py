"""coke"""
def main():
    """input"""
    price = int(input())
    keecap = int(input())
    newprice = int(input())
    want = int(input())

    if not price or not want:
        pay = 0
    elif not keecap:
        pay = want * price
    else:
        pay = 0
        cap = 0

        for _ in range(want):
            if cap and not cap % keecap:
                cap += 1
                pay += newprice
            else:
                pay += price
                cap += 1
    print(pay)


main()
