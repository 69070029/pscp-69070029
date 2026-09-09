"""hotel"""
def main():
    """input"""
    num = input()

    if int(num[0]) > 5:
        first = '9'
    elif int(num[1]) > 5:
        first = '10'
    elif int(num[2]) > 5:
        first = '11'
    elif int(num[3]) > 5:
        first = '12'
    elif int(num[4]) > 5:
        first = '14'
    else:
        first = '13'

    if num == num[::-1]:
        if int(num[0]) + int(num[4]) > 5:
            sec = '1'
        elif int(num[1]) * int(num[3]) > 5:
            sec = '2'
        else:
            sec = '0'
    else:
        if int(num[4]) and (int(num[0]) // int(num[4]) > 5):
            sec = '1'
        elif int(num[1]) - int(num[4]) > 5:
            sec = '2'
        else:
            sec = '0'

    if int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) > 25:
        third = '1'
    elif int(num[0]) * int(num[1]) * int(num[2]) * int(num[3]) * int(num[4]) > 55:
        third = '2'
    else:
        third = '0'

    print(first + sec + third)

main()
