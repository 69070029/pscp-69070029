"""pickthemagain"""
num = list(map(int, input().split()))
results = []

for i in range(len(num) - 1, -1, -1):
    if not num[i] % 3 or not num[i] % 5:
        results.append(num[i])

if len(results) > 0:
    print(*results, sep="\n")
else:
    print("Nope")
