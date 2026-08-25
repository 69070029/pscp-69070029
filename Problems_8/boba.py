"""boba"""
def main():
    """input"""
    boba = input().split()
    sweet = input().split()

    tea = {
        "R": {"1": 12, "2": 18, "3": 25},
        "T": {"1": 15, "2": 20, "3": 30},
        "M": {"1": 10, "2": 15, "3": 20}
    }

    cal = tea[sweet[0]][sweet[1]] * float(sweet[2])

    if boba[0] == "H":
        cal += float(boba[1]) * 5
    elif boba[0] == "O":
        cal += float(boba[1]) * 3
    else:
        cal += float(boba[1]) * 2

    if cal.is_integer():
        print(int(cal))
    else:
        print(cal)

main()
