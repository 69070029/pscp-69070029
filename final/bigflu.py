"""big flu"""
row, col = map(int, input().split())
live_r, live_c = map(int, input().split())

taorai = int(input())
infected = [list(map(int, input().split())) for _ in range(taorai)]

safe = 0

for i in range(row):
    for j in range(col):
        risk = False

        for r, c in infected:
            if abs(i - r) <= 2 and abs(j - c) <= 2:
                risk = True
                break

        if not risk:
            safe += 1

ans = 0

for r, c in infected:
    if live_r == r and live_c == c:
        ans = max(ans, 100)
    elif abs(live_r - r) <= 1 and abs(live_c - c) <= 1:
        ans = max(ans, 60)
    elif abs(live_r - r) <= 2 and abs(live_c - c) <= 2:
        ans = max(ans, 20)

print(safe)
print(f"{ans}%")
