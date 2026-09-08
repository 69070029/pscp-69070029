"""x_shape"""
def main():
    """input"""
    size, letter = input().split()
    size = int(size)
    rahus = ord(letter)
    middle = (size // 2) + 1

    for i in range(size):
        line = i + 1
        for j in range(size):
            if i == j or i + j == size - 1:
                if letter == "#":
                    print(letter, end="")
                else:
                    print(chr(rahus + abs(line - middle)), end="")
            else:
                print("-", end="")
        print()
main()
