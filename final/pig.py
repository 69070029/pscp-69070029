"""pig"""
pair = int(input())
makkwa = []

num = list(map(int, input().split()))

for _ in range(pair):
    compare = []
    for _ in range(2):
        compare.append(num[0])
        num.remove(num[0])
    makkwa.append(max(compare))

if pair > 1:
    print(*makkwa, sep = " + ", end = " = ")
print(sum(makkwa))
