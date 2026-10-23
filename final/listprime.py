"""list prime"""
n = int(input())

every = [True] * (n + 1)
every[0] = every[1] = False

for i in range(2, int(n**0.5) + 1):
    if every[i]:
        for j in range(i * i, n + 1, i):
            every[j] = False

if every[n]:
    print("Yes")
    print(*[i for i in range(2, n + 1) if every[i]])
else:
    print("No")
