"""overlapping?"""
def main():
    """input"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())

    x11 = x1 + r1
    x22 = x2 - r2

    if x11 > x22:
        ans = "overlapping"
    elif x1 == x2 and y1 == y2:
        ans = "overlapping"
    else:
        ans = "no overlapping"

    print(ans)

main()
