"""SqFree"""
last = int(input())
total = 0

for num in range(1, last + 1):
    sqfree = True
    for i in range(2, int(num**0.5) + 1):
        if not num % i**2:
            sqfree = False
            break

    if sqfree:
        total += 1

print(total)
