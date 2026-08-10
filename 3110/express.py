"""EXPRESS"""
def main():
    """input"""
    path = input().split()
    weight = float(input())

    if path[0] == 'BKK':
        if path[1] == 'CNX':
            pay = 10 + (weight * 30)
            print(f"{pay:.2f}")
        elif path[1] == 'PKT':
            pay = 25 + (weight * 50)
            print(f"{pay:.2f}")

    elif path[0] == 'CNX' and path[1] == 'UBP':
        pay = 15 + (weight * 40)
        print(f"{pay:.2f}")

    elif path[0] == 'UBP':
        if path[1] == 'BKK':
            pay = 20 + (weight * 40)
            print(f"{pay:.2f}")
        elif path[1] == 'PKT':
            pay = 40 + (weight * 70)
            print(f"{pay:.2f}")

    elif path[0] == 'PKT' and path[1] == 'CNX':
        pay = 30 + (weight * 60)
        print(f"{pay:.2f}")

    else:
        print("Error")

main()
