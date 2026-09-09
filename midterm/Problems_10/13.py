"""hotel"""
num = input()

if int(num[0]) > 5:
    FIRST = '9'
elif int(num[1]) > 5:
    FIRST = '10'
elif int(num[2]) > 5:
    FIRST = '11'
elif int(num[3]) > 5:
    FIRST = '12'
elif int(num[4]) > 5:
    FIRST = '14'
else:
    FIRST = '13'

if num == num[::-1]:
    if int(num[0]) + int(num[4]) > 5:
        SEC = '1'
    elif int(num[1]) * int(num[3]) > 5:
        SEC = '2'
    else:
        SEC = '0'
else:
    if int(num[4]) and (int(num[0]) // int(num[4]) > 5):
        SEC = '1'
    elif int(num[1]) - int(num[4]) > 5:
        SEC = '2'
    else:
        SEC = '0'

if int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) > 25:
    THIRD = '1'
elif int(num[0]) * int(num[1]) * int(num[2]) * int(num[3]) * int(num[4]) > 55:
    THIRD = '2'
else:
    THIRD = '0'

print(FIRST + SEC + THIRD)
