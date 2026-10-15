"""race"""
racer, rounds = map(int, input().split())
speed = [int(input()) for _ in range(racer)]

speed = sorted(speed)
fastest = speed[0]
eliminated = []

for person in speed:
    if person == fastest:
        continue

    for i in range(1, rounds + 1):
        if fastest * i <= person * (i-1):
            eliminated.append(person)
            break

print(racer - len(eliminated))
