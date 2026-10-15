"""bread"""
wide, high, _, _ = map(int, input().split())
tung = list(map(int, input().split()))
non = list(map(int, input().split()))

tung.insert(0, 0)
tung.append(wide)
non.insert(0, 0)
non.append(high)

dai_m = [] #tung/m
dai_n = []

for i,cut_m in enumerate(tung[1:]):
    dai_m.append(cut_m - tung[i])

for j,cut in enumerate(non[1:]):
    dai_n.append(cut - non[j])

max1 = 0
max2 = 0

for lek in dai_m:
    for num in dai_n:
        bread = lek * num

        if bread >= max1:
            max2 = max1
            max1 = bread
        elif bread > max2:
            max2 = bread

print(max1, max2)
