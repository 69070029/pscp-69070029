"""DICE"""
def main():
    """input"""
    tai = int(input())
    result = int(input())

    if tai < 1 or tai > 6 or result < 1 or result > 6:
        ans = "Invalid"
    elif tai == result:
        ans = "Correct!"
    else:
        ans = "Wrong!"

    print(ans)
main()
