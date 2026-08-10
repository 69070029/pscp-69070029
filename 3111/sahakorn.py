"""sahakornrongrian"""
def main():
    """input"""
    member = input()
    howmuch = int(input())

    pay = 0

    for _ in range(howmuch):
        price = float(input())
        pay += price

    if member == "Y":
        pay = pay * 0.95
    elif member == "N" and pay >= 500:
        pay = pay * 0.97

    print(f"{pay:.2f}")

main()
