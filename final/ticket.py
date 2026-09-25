"""ticket"""
seat = int(input())
PRICE = 150

while seat > 0:
    age, need = map(int, input().split())

    if age < 15:
        print(-1)
        continue
    if seat < need:
        print(-2)
        continue

    if 15 <= age <= 22:
        print(int(need * PRICE * 0.8), seat - need, sep=" ")
        seat -= need
    elif age >= 60:
        print(int(need * PRICE * 0.5), seat - need, sep=" ")
        seat -= need
    else:
        print(need * PRICE, seat - need, sep=" ")
        seat -= need
