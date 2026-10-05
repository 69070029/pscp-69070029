"""Point Sorting"""
taorai = int(input())

for _ in range(taorai):
    keetua = int(input())

    box = [list(map(int, input().split())) for _ in range(keetua)]
    box = sorted(box, key=sum)

    for j in range(keetua - 1):
        if sum(box[j]) == sum(box[j + 1]):
            if box[j][1] < box[j + 1][1]:
                box[j], box[j + 1] = box[j + 1], box[j]

    for row in box:
        print(*row)
