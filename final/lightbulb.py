"""light bulb"""
taorai = int(input())
height = []

for _ in range(taorai):
    height.append(int(input()))

height = sorted(height)

walk = 0
total = 0

for pole in height:
    total += pole
    walk += 2 * total

print(walk)
