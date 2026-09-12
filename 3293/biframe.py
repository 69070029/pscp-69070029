"""bigframe"""
message = []

for _ in range(5):
    message.append(input())

longest = len(max(message, key=len))

border = "*" * (longest + 4)

print(border)

for word in message:
    print("*", word, " " * (longest - len(word)) + "*")

print(border)
