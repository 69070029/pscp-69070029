"""Caesar v2"""
sentence = input()

words = ["what", "when", "why", "which", "this", "there",
         "where", "the", "is", "am", "are", "you", "we",
         "they", "he", "she", "it"]

for shift in range(26):
    result = ""

    for char in sentence:
        if "a" <= char <= "z":
            result += chr((ord(char) + shift) % 26 + ord("a"))
        if "A" <= char <= "Z":
            result += chr((ord(char) + shift) % 26 + ord("A"))
        else:
            result += char

    found = False

    for word in result.split():
        if word.lower() in words:
            found = True
            break

    if found:
        break

print(result)
