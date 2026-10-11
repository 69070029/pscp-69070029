"""card"""
def main():
    """input"""
    card = input().upper()

    if card[:-1].isnumeric():
        first = card[:-1]
    elif card[:-1] == "A":
        first = "ace"
    elif card[:-1] == "J":
        first = "jack"
    elif card[:-1] == "Q":
        first = "queen"
    else:
        first = "king"

    if card[-1] == "D":
        last = "diamonds"
    elif card[-1] == "H":
        last = "hearts"
    elif card[-1] == "S":
        last = "spades"
    else:
        last = "clubs"

    print(f"{first} of {last}")
main()
