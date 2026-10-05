"""magic coin"""
venue = int(input())
coins = [list(map(int, input().split())) for _ in range(venue)]

fire = 0
water = 0
earth = 0

for i in range(venue):
    fire += (max(coins[i][0], coins[i][3]))
    water += (max(coins[i][1], coins[i][4]))
    earth += (max(coins[i][2], coins[i][5]))

print(f"Total: {fire + water + earth}")
print(f"Fire: {fire}")
print(f"Water: {water}")
print(f"Earth: {earth}")

if fire > water+earth:
    print("Bonus: YES")
else:
    print("Bonus: NO")
