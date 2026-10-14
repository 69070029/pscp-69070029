"""bullet"""
taorai = int(input())
bullet = []
ans = False

for _ in range(taorai):
    x, y, d = map(int, input().split())
    bullet.append((x, y, d))

for tx in range(1000):
    for ty in range(1000):
        for x, y, d in bullet:
            if (tx - x)**2 + (ty- y)**2 != d**2:
                break
        else:
            print(tx, ty)
            ans = True
            break
    if ans:
        break
