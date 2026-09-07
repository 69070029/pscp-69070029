"""frog"""
def main():
    """input"""
    jump, goal = map(int, input().split())

    distance = 0
    attempt = 0

    while distance < goal:
        distance += jump
        attempt += 1

        jump -= 2
        if jump <= 0:
            break

    if distance >= goal:
        print(attempt)
    else:
        print(-1)

main()
