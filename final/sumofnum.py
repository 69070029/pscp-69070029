"""sum of number"""
want = int(input())
total = 0

while total != want:
    num = int(input())
    if num == -1:
        break
    total += num

print(total)
