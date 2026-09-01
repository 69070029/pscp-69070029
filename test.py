print(ord('a'))
print(ord('z'))

letter = ord(input()) + 1
if letter > ord('z'):
    letter -= (26 * (letter % 122))

    print(letter)