"""Suvarnabhumi Airport Parking"""
import math

def main():
    """tumrai"""
    park = input()
    leave = input()
    
    if not "." in (park) or not "." in (leave):
        print("ERROR")
        return

    park = park.split('.')
    leave = leave.split('.')
    
    if (len(park) != 2 or len(leave) != 2) or (len(leave[1]) != 2 or len(park[1]) != 2):
        print("ERROR")
        return

    h1, m1 = int(park[0]), int(park[1])
    h2, m2 = int(leave[0]), int(leave[1])

    if not (0 <= h1 <= 23 and 0 <= m1 <= 59 and 0 <= h2 <= 23 and 0 <= m2 <= 59):
        print("ERROR")
        return

    end = h2 * 60 + m2
    start = h1 * 60 + m1

    if end < start:
        end += 24 * 60

    diff = end - start

    if diff <= 15:
        pay = "FREE"
    else:
        hour = math.ceil(diff / 60)

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
        else:
            pay = 250

    print(pay)

main()
