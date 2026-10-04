"""giraffe"""
num = int(input())
neck = [int(input()) for _ in range(num)]
high = 0

if num == 1:
    high += 1
else:
    for i, gir in enumerate(neck):
        if not i:
            if gir > neck[i + 1]:
                high += 1
        elif i == len(neck) - 1:
            if gir > neck[i - 1]:
                high += 1
        else:
            if gir > neck[i + 1] and gir > neck[i - 1]:
                high += 1
print(high)
