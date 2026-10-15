"""chair queue"""
_, _ = map(int, input().split())
queue = list(map(int, input().split()))
chair = list(map(int, input().split()))

chair_idx = [x-1 for x in chair]

for kontee in chair_idx:
    height = 0

    for i in range(kontee):
        if not kontee:
            break
        height = max(height, queue[i] - queue[kontee] + 1)

    print(height)
