"""bigframe"""
message = []

for _ in range(5):
    message.append(input())

print("*" * (len(max(message, key=len)) + 4))

for word in message:
    print("*", word, "*", sep=" ")

print("*" * (len(max(message, key = len)) + 4))
