"""sahakornrongrian"""
from decimal import Decimal, ROUND_HALF_UP

def main():
    """input"""
    member = input()
    howmuch = int(input())

    pay = Decimal("0")

    for _ in range(howmuch):
        price = Decimal(input())
        pay += price

    if member == "Y":
        pay = pay * Decimal("0.95")
    elif member == "N" and pay >= Decimal("500"):
        pay = pay * Decimal("0.97")

    pay = pay.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print(pay)

main()
