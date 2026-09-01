<<<<<<< HEAD
print(ord('a'))
print(ord('z'))

letter = ord(input()) + 1
if letter > ord('z'):
    letter -= (26 * (letter % 122))

    print(letter)
=======
message = input()

print(ord(message))
>>>>>>> 856600fc2f10334e012bd2f20fe318bcf28bd6fb
