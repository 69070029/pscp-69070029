"""ink"""
def main():
    """import n input"""
    import math

    spd_ppl = list(map(int, input().split()))
    pi = 3.1416

    speed = (spd_ppl[0] / pi)**0.5

    for _ in range(spd_ppl[1]):
        where = list(map(int, (input()).split()))

        distance = (where[0]**2 + where[1]**2)**0.5 #ถูกแล้ว

        when = int(math.ceil(distance / speed))

        print(distance)

main()
