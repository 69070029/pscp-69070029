"""ticket"""
seat = int(input())
price = 150

try:
    while True:
        age, need = map(int, input().split())

        if not seat:
            print(-2)
            break
        elif seat < need:
            print(-2)
            continue
        elif age < 15:
            print(-1)
            continue

        if 15 <= age <= 22:
            print(int(need * price * 0.8), seat - need, sep=" ")
            seat -= need
        elif age >= 60:
            print(int(need * price * 0.5), seat - need, sep=" ")
            seat -= need
        else:
            print(need * price, seat - need, sep=" ")
            seat -= need

except EOFError:
    pass
