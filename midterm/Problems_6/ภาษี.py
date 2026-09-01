"""ภาษี"""
def main():
    """input"""
    year = int(input())
    cc = int(input())

    if cc <= 1500:
        if year <= 1990:
            print(1250)
        elif year >= 2000:
            print(1000)
        else:
            print(1100)
    elif cc > 2000:
        if year <= 1990:
            print(2000)
        elif year >= 2000:
            print(1500)
        else:
            print(1700)
    else:
        if year <= 1990:
            print(1400)
        elif year >= 2000:
            print(1200)
        else:
            print(1300)

main()
