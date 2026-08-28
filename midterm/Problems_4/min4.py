"""minimum (4)"""
def main():
    """input"""
    loop = int(input())

    n_list = []

    for _ in range(loop):
        number = int(input())
        n_list.append(number)

    for _ in range(loop - 1):
        n_list.remove(max(n_list))

    print(*n_list)

main()
