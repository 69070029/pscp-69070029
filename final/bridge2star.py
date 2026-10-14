"""bridge"""
distance, taorai = map(int, input().split())

bridge = []
count_box = []

for _ in range(taorai):
    start, end = map(int, input().split())
    bridge.append((start, end))

for x in range(distance + 1):
    count = 0

    for a,b in bridge:
        if a < x + 0.5 < b:
            count += 1

    count_box.append(count)

print(max(count_box))
