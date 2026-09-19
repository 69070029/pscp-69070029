"""arrow"""
RL = input()
size = int(input())

for word in RL:
    if word == "R":
        box = []
        for i in range(1, size + 1):
            ans = " " * abs((i-1) * 2) + "*" * abs(i-size-1)
            print(ans)
            box.append(ans)
        for ans in box[-2::-1]:
            print(ans)
    else:
        box = []
        for i in range(1, size + 1):
            ans = " " * abs(i-size) + "*" * abs(i-size-1)
            print(ans)
            box.append(ans)
        for ans in box[-2::-1]:
            print(ans)

    if word != RL[-1]:
        print()
