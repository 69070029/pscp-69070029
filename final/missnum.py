"""missing number"""
current = 0

last = int(input())

for i in range(1, last + 1):
    num = int(input())

    if i != 1 and num != current + 1:
        for j in range(1, num - current + 1):
            print(num + j)

    current = num
