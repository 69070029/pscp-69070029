"""ink"""
import math

def main():
    """import n input"""

    spd_ppl = list(map(int, input().split()))
    pi = 3.1416


    for _ in range(spd_ppl[1]):
        where = list(map(int, (input()).split()))

        when = math.ceil((pi * (where[0]**2 + where[1]**2)) / spd_ppl[0])

        print(when)

main()
