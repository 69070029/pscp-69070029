"""busstop I"""
cap = int(input())
n = int(input())

stops = [[] for _ in range(n + 1)]

for _ in range(n):
    data = list(map(int, input().split()))
    stop_id = data[0]
    passengers = data[1:]
    stops[stop_id] = passengers

bus = []
goal = 0

for current in range(1, n + 1):
    still_on = []
    for person in bus:
        if person == current:
            goal += 1
        else:
            still_on.append(person)
    bus = still_on

    for person in stops[current]:
        if person > current:
            if len(bus) < cap:
                bus.append(person)
            else:
                break

print(goal)
