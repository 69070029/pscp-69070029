"""tug of war"""
a = 0
b = 0
for _ in range(10):
    pull = int(input())
    a += pull

for _ in range(10):
    pull2 = int(input())
    b += pull2

if a < b:
    print("A")
elif a > b:
    print("B")
else:
    print("AB")
