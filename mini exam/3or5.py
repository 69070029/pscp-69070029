"""Divide3Or5"""
num = int(input())

total = 0

for i in range(1, num + 1):
    if not i % 5 or not i % 3:
        total += i

print(total)
