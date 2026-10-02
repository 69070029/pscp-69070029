"""run"""
day, goal = map(int, input().split())
run = list(map(int, input().split()))

distance = 0

for i in range(day):
    distance += run[i]

    if distance >= goal:
        print(i + 1)
        break

if distance < goal:
    print(-1)
