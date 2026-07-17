"""หาร 10"""
def main():
    """input"""
    number = input()
    new_num = int(number[:-1] + "0")

    while new_num >= 0:
        print(new_num, end=" ")
        new_num -= 10
        if not new_num:
            print(0)
            break
main()
