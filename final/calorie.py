"""calorie"""
menu = {
    1: 100,
    2: 120,
    3: 200,
    4: 60
}

total = 0

while True:
    num = int(input())
    if num == 5:
        break
    total += menu[num]

print("Bye Bye")
print("Total Calories:", total)
