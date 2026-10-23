"""units"""
def main():
    """input"""
    number = float(input())
    new = input()
    old = input()

    if old == "NIU":
        sen = number / 12 / 2 / 4 /20
    elif old == "KUEP":
        sen = number / 2 / 4 / 20
    elif old == "SOK":
        sen = number / 4 / 20
    elif old == "WA":
        sen = number / 20
    else:
        sen = number

    if new == "NIU":
        sol = sen * 20 * 4 * 2 * 12
    elif new == "KUEP":
        sol = sen * 20 * 4 * 2
    elif new == "SOK":
        sol = sen * 20 * 4
    elif new == "WA":
        sol = sen * 20
    else:
        sol = sen

    print(f"{sol:.4f}")
main()
