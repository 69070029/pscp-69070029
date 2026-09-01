"""leap year"""
def main():
    """input"""
    year = int(input())

    if not year % 4:
        if not year % 400:
            print("yes")
        elif not year % 100 and year > 1582:
            print("no")
        else:
            print("yes")
    else:
        print("no")

main()
