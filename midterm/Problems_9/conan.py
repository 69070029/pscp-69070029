"""CONAN"""
def main():
    """input"""
    word = input()
    move = int(input())

    word_2 = ""

    for i in range(len(word)):
        if ord(word[i]) + move > 26:
            new = chr((ord(word[i]) + move) % 26)
            word_2 += new
        else:
            new = chr(ord(word[i]) + move)
            word_2 += new

    print(word_2)

main()
