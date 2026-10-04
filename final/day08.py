"""reverse"""
text = ""
message = []

while text != "NULL":
    text = input()
    message.append(text)

message.remove("NULL")
message.reverse()
print(*message, sep = "\n")
