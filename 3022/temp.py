"""temp"""
def main():
    """input"""
    temp = float(input())
    CFKR1 = input()
    CFKR2 = input()

    if CFKR1 == "R":
        C = ((5/9) * temp) - 273.15
    elif CFKR1 == "K":
        C = temp - 273.15
    elif CFKR1 == "F":
        C = (temp - 32) * (5/9)
    else:
        C = temp

    if CFKR2 == "R":
        ans = (C + 273.15) * (9/5)
    elif CFKR2 == "K":
        ans = C + 273.15
    elif CFKR2 == "F":
        ans = C * (9/5) + 32
    else:
        ans = C

    print(f"{ans:.2f}")


main()
