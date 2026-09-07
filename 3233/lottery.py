"""lottery"""
def main():
    """input"""
    w_letter, w_num = input().split()
    b_letter, b_num = input().split()

    if w_letter == b_letter:
        if w_num == b_num:
            print(1000000)
        elif w_num[-3:] == b_num[-3:]:
            print(2000)
        elif w_num[-2:] == b_num[-2:]:
            print(1000)
        else:
            print(20)
    else:
        if w_num == b_num:
            print(100000)
        elif w_num[-3:] == b_num[-3:]:
            print(200)
        elif w_num[-2:] == b_num[-2:]:
            print(100)
        else:
            print(0)

main()
