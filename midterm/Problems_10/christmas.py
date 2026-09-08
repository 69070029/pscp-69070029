"""christmas"""
def main():
    """input"""
    first, total = input().split()
    total = int(total)

    color = []

    if first == "R":
        color.append("Red")
    elif first == "G":
        color.append("Green")
    elif first == "B":
        color.append("Blue")

    for _ in range(total - 1):
        if color[-1] == "Red":
            color.append("Green")
        elif color[-1] == "Green":
            color.append("Blue")
        else:
            color.append("Red")

    print(*color)

main()
