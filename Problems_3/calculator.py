"""calculator"""
def main():
    """input"""
    num = int(input())
    n = 0

    if num == 1:
        print(1)
    else:
        for i in range(1, num + 1):
            n += len(str(i)) + 1
        print(n)

main()
