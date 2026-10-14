"""faisong"""
fai = int(input())
light = [False] * 360

for _ in range(fai):
    start, end = map(int, input().split())

    if start < end:
        for i in range(start, end + 1):
            light[i] = True
    else:
        for i in range(start, 360):
            light[i] = True
        for i in range(end + 1):
            light[i] = True

tid = []
count = 0

light = light + light

if all(light):
    print(360)
else:
    for x in light:
        if x:
            count += 1
        else:
            tid.append(count)
            count = 0

    print(max(tid) - 1)
