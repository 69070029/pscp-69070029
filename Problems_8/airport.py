"""Suvarnabhumi Airport Parking"""
import math

def main():
    """tumrai"""
    park = input().split('.')
    leave = input().split('.')

    h1 = int(park[0])
    m1 = int(park[1])
    h2 = int(leave[0])
    m2 = int(leave[1])

    if not (0 <= h1 <= 23 and 0 <= m1 <= 59 and 0 <= h2 <= 23 and 0 <= m2 <= 59):
        pay = "ERROR"
    else:
        minutes = (h2 * 60 + m2) - (h1 * 60 + m1)

        if minutes < 0:
            minutes += 24 * 60

        if minutes <= 15:
            pay = "FREE"
        else:
            hour = math.ceil(minutes / 60)

            price = {
                1: 25,
                2: 50,
                3: 80,
                4: 110,
                5: 145,
                6: 180,
            }

            if hour in price:
                pay = price[hour]
            elif hour > 24:
                pay = "ERROR"
            else:
                pay = 250

    print(pay)

main()
