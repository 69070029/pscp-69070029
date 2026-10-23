"""dart"""
taorai = int(input())
score = 0

for _ in range(taorai):
    x, y = map(int, input().split())
    d = (x**2 + y**2)**0.5

    if d <= 2:
        score += 5
    elif 2 < d <= 4:
        score += 4
    elif 4 < d <= 6:
        score += 3
    elif 6 < d <= 8:
        score += 2
    elif 8 < d <= 10:
        score += 1

print(score)
