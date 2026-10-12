"""card"""
card = input().upper()

first = card[:-1]
last = card[-1]

front = {
    "A": "Ace",
    "J": "Jack",
    "Q": "Queen",
    "K": "King"
}

back = {
    "D": "Diamonds",
    "H": "Hearts",
    "S": "Spades",
    "C": "Clubs"
}

print(f"{front.get(first, first)} of {back.get(last)}")
