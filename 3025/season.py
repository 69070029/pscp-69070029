"""doc"""
def main():
    """doc"""
    month = int(input())
    day = int(input())
    season1 = month == 3 and day < 21
    season2 = month == 6 and day < 21
    season3 = month == 9 and day < 21
    season4 = month == 12 and day < 21
    if (month == 12 and day >=21) or month == 1 or month == 2 or season1:
        print("winter")
    elif (month == 3 and day >=21) or month == 4 or month == 5 or season2:
        print("spring")
    elif (month == 6 and day >= 21) or month == 7 or month == 8 or season3:
        print("summer")
    elif (month == 9 and day >= 21) or month == 10 or month ==11 or season4:
        print("fall")

main()
