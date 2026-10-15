"""car"""
taorai = int(input())
meearai = []

for _ in range(taorai):
    p, v = map(int, input().split())
    meearai.append((p, v))

meearai.reverse() #cheap -> expensive

nosold = 0
current = meearai[0][1]

for p, v in meearai:
    if v < current:
        nosold += 1
    else:
        current = v

print(nosold)
