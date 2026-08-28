"""ONLINE"""
def main():
    """input"""
    base = float(input())
    bonus = float(input())
    day = int(input())

    if day > 3:
        total = 1.5 * (base + bonus)
    else:
        total = base + bonus

    if total >= 1500:
        rank = 5
    elif total >= 1000:
        rank = 4
    elif total >= 500:
        rank = 3
    elif total >= 200:
        rank = 2
    else:
        rank = 1

    if rank == 5 and day >= 7:
        spc = 99
    elif rank == 4 and bonus > 300:
        spc = 88
    else:
        spc = 0

    print(f"{total:.0f}")
    print(rank)
    print(spc)
main()
