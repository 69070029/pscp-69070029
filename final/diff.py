"""A - B"""
n = int(input())
m = int(input())
a = set()
b = set()

for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())

a = a - b

print(*sorted(a))
