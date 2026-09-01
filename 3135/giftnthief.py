"""gift n thief"""
def main():
    """input"""
    num, skip, thief = map(int, input().split())
    posi = 1
    get = 1

    while posi != thief:
        posi = (posi + skip) % num

        if posi == thief:
            get += 1
            break
        if posi == 1:
            break

        get += 1

    print(get)
main()
