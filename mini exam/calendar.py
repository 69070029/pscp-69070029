"""calendar"""
day = int(input())
month = int(input())
year = int(input())

if year < 2569 or (year == 2569 and (month < 10 or (month == 10 and day <= 2))):
    date = year * 360 + month * 30 + day
    TORN = 2569 * 360 + 10 * 30 + 2

    print(abs(date - TORN))
else:
    print(0)
