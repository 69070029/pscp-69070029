"""ron chib hai"""
taorai = int(input())
temp = list(map(float, input().split()))
more = 0

avg = sum(temp) / len(temp)

for i in range(taorai):
    if temp[i] > avg:
        more += 1

print(f"{avg:.2f}")
print(more)
