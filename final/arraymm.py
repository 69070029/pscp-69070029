"""array mae meung"""
row = -1
col = -1

box = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    if sum(box[i]) % 2:
        row = i
        break

for j in range(5):
    if sum(num[j] for num in box) % 2:
        col = j
        break

print(row, col)
