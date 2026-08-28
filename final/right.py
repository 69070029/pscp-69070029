"""liao kwah"""
def main():
    """input"""
    width = int(input())
    height = int(input())

    mid = (height // 2) + 1
    t_width = "*" * width

    for i in range(height):
        if (i + 1) <= mid:
            print((" " * i) + t_width)
        else:
            print((" " * abs((i+1) - height)) + t_width)

main()
