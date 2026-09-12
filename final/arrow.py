"""arrow"""
RL = input()
size = int(input())

for word in RL:
    box = []
    for i in range(size * 2 - 1):
        if i <= (size - 1):
            line = (" " * (2 * i)) + ("*" * abs(size - i))
            box.append(line)
            print(line)
        else:
            box.reverse()
            line = box[abs(size - i)]
            print(line)