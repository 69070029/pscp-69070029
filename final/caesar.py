"""Caesar v2"""
import string

sentence = input()

words = ["what", "when", "why", "which", "this", "there",
         "where", "the", "is", "am", "are", "you", "we",
         "they", "he", "she", "it"]

best_result = ""
max_count = 0

for shift in range(26):
    result = ""

    for char in sentence:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            result += char

    count = 0

    for word in result.split():
        if word.strip(string.punctuation).lower() in words:
            count += 1

    if count > max_count:
        max_count = count
        best_result = result

print(best_result)
