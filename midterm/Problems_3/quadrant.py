"""quadrant"""
def main():
    """input"""
    x = int(input())
    y = int(input())

    if not x:
        if not y:
            ans = "O"
        else:
            ans = "Y"
    elif not y and x:
        ans = "X"
    elif x > 0 and y > 0:
        ans = "Q1"
    elif x < 0 < y:
        ans = "Q2"
    elif x < 0 and y < 0:
        ans = "Q3"
    else:
        ans = "Q4"

    print(ans)

main()
