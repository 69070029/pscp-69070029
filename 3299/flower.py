"""garden"""
l, goal = map(int, input().split())

total_in_l = 0
layer = 0

while total_in_l < goal:
    layer += 1
    tyang_in_l = layer * l
    total_in_l = tyang_in_l * (tyang_in_l + 1) // 2

print(layer)
