"""arrow"""
RL = input()
size = int(input())

middle = size - 1
total = size * 2 - 1

for word in RL:
    if word == "R":
        dokjun = []
        for i in range(total): #0 - 9
            if i <= middle:
                ans = ((" " * (i * 2)) + ("*" * (size - i)))
                dokjun.append(ans)
                print(ans)
        for i in reversed(range(len(dokjun) - 1)):
            print(dokjun[i])
    else:
        
            