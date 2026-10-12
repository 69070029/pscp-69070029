"""bird"""
taorai = int(input())
height = list(map(int, input().split()))

tall = 0

for i in range(taorai):
    if taorai == 1:
        tall += 1
        break

    if not i:
        if height[i] > height[i + 1]:
            tall += 1
    elif i == taorai - 1:
        if height[i] > height[i - 1]:
            tall += 1
    else:
        if height[i] > height[i - 1] and height[i] > height[i + 1]:
            tall += 1

print(tall)
