<<<<<<< HEAD
"""arcade of time"""
def main():
    """input"""
    shop, check = map(int, input().split())

    for _ in range(shop):
        open, close = map(int, input().split())

    c_time = list(map(int, input().split()))
    print(len(c_time))
    #for _ in range(len(c_time))


main()
=======
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
>>>>>>> 0e3d4440b5f35d3b8a4ee55e92e46594ef91bf7c
