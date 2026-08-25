"""ramen"""
def main():
    '''input'''
    size, pisedmai = input().split()
    topping = input().split()

    price = {
        "S": {"R": 60, "T": 80},
        "M": {"R": 80, "T": 100},
        "L": {"R": 100, "T": 120}
    }

    pay = price[size][pisedmai]

    if topping[0] == "P":
        pay += 15 * int(topping[1])
    elif topping[0] == "E":
        pay += 10 * int(topping[1])

    print(pay)

main()
