"""ticket"""
def main():
    """input"""
    age, day = map(str, input().split())
    age = int(age)
    if age < 5:
        print('0')
    elif day == 'Wed':
        if 5 <= age <= 18:
            print('50')
        else:
            print('75')
    else:
        if 5 <= age <= 18:
            print('100')
        else:
            print('150')

main()
