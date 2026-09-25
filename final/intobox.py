"""sai klong"""
w, l, m, n = map(int, input().split())
box = []

for i in range(m, n + 1):
    total = (w % i) * (l % i)
    box.append(total)

print(min(box))
