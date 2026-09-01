"""hello"""
def main():
    """yea"""
    typeo, year, money  = map(str, input().split())
    money = int(money)
    year = int(year)

    if typeo == "M":
        if year <= 5:
            bonus = (money * 0.06)+1500
        elif year > 10:
            bonus = (money * 0.10)+1500
        else:
            bonus =(money * 0.08)+1500
    elif typeo == "B":
        if year <= 5:
            bonus = (money * 0.05)+1000
        elif year > 10:
            bonus = (money * 0.07)+1000
        else:
            bonus = (money * 0.06)+1000
    else:
        if year <= 5:
            bonus = (money * 0.04)+500
        elif year > 10:
            bonus = (money * 0.06)+500
        else:
            bonus = (money * 0.05)+500

    print(int(bonus))

main()
