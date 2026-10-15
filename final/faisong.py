"""faisong"""
fai = int(input())
light = [False] * 360

for _ in range(fai):
    start, end = map(int, input().split())

    if start < end:
        for i in range(start, end):
            light[i] = True
    else:
        for i in range(start, 360):
            light[i] = True
        for i in range(end):
            light[i] = True

if all(light):
    print(360)
else:
    light = light + light
    count = 0
    ans = 0

    for x in light:
        if x:
            count += 1
            ans = max(ans, count)
        else:
            count = 0

    print(ans)
