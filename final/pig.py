#pig
pair = int(input())
makkwa = []

num = list(map(int, input().split()))

for i in range(pair * 2):
    if i % 2: continue

    makkwa.append(max(num[i], num[i + 1]))

result = " + ".join(str(makkwa))
print(makkwa)
print(result)