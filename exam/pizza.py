"""pizza"""
def main():
    """input"""
    ppl = int(input())
    each = int(input())
    perbox = int(input())

    eattaorai = ppl * each

    keebox = eattaorai // perbox

    if eattaorai % perbox:
        keebox += 1

    remain = (keebox * perbox) - eattaorai

    print(eattaorai)
    print(keebox)
    print(remain)

main()
