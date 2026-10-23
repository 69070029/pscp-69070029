"""stats"""
def main():
    """input"""
    taorai = int(input())

    ruam = 0
    maksud = 0
    noisud = 0

    for _ in range(1):
        number = int(input())
        ruam += number
        maksud += number
        noisud += number

    for _ in range(1, taorai):
        number = int(input())
        ruam += number

        if number > maksud:
            maksud = number

        if number < noisud:
            noisud = number

    chalia = ruam / taorai

    print(f"MIN: {noisud:.3f}")
    print(f"MAX: {maksud:.3f}")
    print(f"AVG: {chalia:.3f}")

main()
