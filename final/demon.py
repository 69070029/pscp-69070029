"""demon slayer"""
demon = [
    ("Spider Demon", 1),
    ("Swamp Demon", 2),
    ("Arrow Demon", 1),
    ("Hand Demon", 2),
    ("Drum Demon", 3),
    ("Mugen Train", 2),
    ("Upper Moon", 3)
]

kill = 0
attack = 0

while kill < 5:
    name, correct = demon.pop(0)
    print(name)
    win = False

    for _ in range(2):
        ans = int(input())
        attack += 1

        if ans == correct:
            win = True
            kill += 1
            print("kill")
            break

    if not win:
        print("back")
        demon.append((name, correct))

print(attack)
