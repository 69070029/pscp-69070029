"""busstop I"""
cap = int(input())
stop = int(input())

current = []

goal = 0

for j in range(stop):
    ppl = list(map(int, input().split()))

    before = len(current)
    current = [x for x in current if x != j + 1]
    goal += before - len(current)

    for i, person in enumerate(ppl):
        if not i:
            continue
        if person > ppl[0]:
            if len(current) == cap:
                break
            current.append(person)

print(goal)
