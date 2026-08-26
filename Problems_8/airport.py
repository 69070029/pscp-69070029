"""Suvarnabhumi Airport Parking"""
import math

def main():
    """tumrai"""
    park = input().split('.')
    leave = input().split('.')

    minutes = (int(leave[0]) * 60 + int(leave[1])) - (int(park[0]) * 60 + int(park[1]))

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
        elif 7 <= hour <= 24:
            pay = 250
        else:
            pay = "ERROR"

    print(pay)

main()
