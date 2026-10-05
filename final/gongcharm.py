"""gong charm"""
taorai = int(input())
charm = sorted([int(input()) for _ in range(taorai)], reverse=True)
same = []
current = charm[0]

for i in range(1, len(charm)):
    if charm[i] == current:
        same.insert(0, charm[i])
    current = charm[i]

if len(same) > 0:
    print(max(same.count(x) for x in same) + 1)
else:
    print(1)
