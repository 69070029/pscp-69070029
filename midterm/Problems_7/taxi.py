"""taxi"""
def main():
    """input"""
    distance = int(input())

    if distance <= 0:
        print(0)
    elif distance <= 1:
        print(35)
    elif distance > 10:
        print((9 * 5) + ((distance - 10) * 8) + 35)
    else:
        print(((distance - 1) * 5) + 35)

main()
