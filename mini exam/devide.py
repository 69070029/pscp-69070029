"""divide 3 or 5"""
last = int(input())
total = 0

for num in range(1, last + 1):
    if not num % 3 or not num % 5:
        total += num

print(total)
