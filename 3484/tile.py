"""tile"""
area, fine = map(int, input().split())
tile = [list(map(int, input().split())) for _ in range(area)]

#row
for r in tile:
    mistake = sum(r)
    count = len(r) - r.count(0)
    r.extend([count, mistake])

count_mistake = sum(r[-2] for r in tile)
total_mistake = sum(r[-1] for r in tile)

count_col = []
mistake_col = []

for j in range(area): #c
    count_c = 0
    mistake_c = 0

    for i in range(area): #r
        if tile[i][j]:
            count_c += 1
            mistake_c += tile[i][j]

    count_col.append(count_c)
    mistake_col.append(mistake_c)

for r in tile:
    print(*r)
print(*count_col)
print(*mistake_col)
print(f"{count_mistake} {total_mistake} {total_mistake * fine:.2f}")
