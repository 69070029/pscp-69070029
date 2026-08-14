"""9999999"""
def main():
    """input"""
    long = int(input())

    rahus1 = input()
    rahus2 = input()
    notnine = 0

    for i in range(long):
        if int(rahus1[i]) + int(rahus2[i]) != 9:
            notnine += 1

    if not notnine:
        print("YES")
    else:
        print(f"NO {notnine}")

main()
