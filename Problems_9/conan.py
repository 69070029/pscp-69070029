"""CONAN"""
def main():
    """input"""
    word = input()
    move = int(input())

    word_num = []
    new = ""

    for i in range(len(word)):
        num = ord(word[i]) + move

        if num > ord('z'):
            num -= (26 * (num // 122))

        word_num.append(num)

    for i in range(len(word_num)):
        final = chr(word_num[i])
        new += final

    print(new)

main()
