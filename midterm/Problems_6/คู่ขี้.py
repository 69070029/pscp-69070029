"""nub lek kee and koo"""
def main():
    """input"""
    kee = []
    koo = []

    for _ in range(3):
        num = int(input())

        if num % 2:
            kee.append(num)
        else:
            koo.append(num)

    print(len(koo))
    print(len(kee))

main()
