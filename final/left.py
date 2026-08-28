"""liao sai"""
def main():
    """input"""
    width = int(input())
    height = int(input())

    cut  = height // 2
    t_width = "*" * width

    for i in range(height):
        print((" " * abs(cut - i)) + t_width)

main()
