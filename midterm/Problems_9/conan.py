"""CONAN"""
def main():
    """input"""
    text = input()
    move = int(input())

    word_num = []
    new = ""

    for word in text:
        num = ord(word) + move

        while num > ord('z'):
            num -= (26 * (num // (122 * 1)))

        word_num.append(num)

    for num in word_num:
        final = chr(num)
        new += final

    print(new)

main()
