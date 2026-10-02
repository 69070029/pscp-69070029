"""price plian"""
day = int(input())
price = list(map(int, input().split()))
diff = []

for i in range(1, day):
    diff.append(abs(price[i] - price[i - 1]))

print(diff.index(max(diff)) + 2, max(diff))
