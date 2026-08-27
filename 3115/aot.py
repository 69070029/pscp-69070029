"""aot"""
num, _ = map(int, input().split())

s_time = [0] * 1441

for _ in range(num):
    start, stop = map(int, input().split())
    s_time[start] += 1
    s_time[stop] -= 1

for i in range(1, 1441):
    s_time[i] += s_time[i - 1]

times = map(int, input().split())

print(*[s_time[t] for t in times])
