"""cave"""
long = int(input())
pantee = list(map(int, input().split()))
drt = input()

#treasure = pantee.index(2)

for move in drt:
    pos = pantee.index(1)
    new_pos = pos + 1 if move == "R" else pos - 1

    if 0 <= new_pos < long:
        if pantee[new_pos] == 2:
            pantee[pos] = 0
            pantee[new_pos] = 1
            break

        pantee[pos], pantee[new_pos] = pantee[new_pos], pantee[pos]

print(*pantee)
