"""Duplicate I"""
g1 = int(input())
g2 = int(input())

member1 = {input() for _ in range(g1)}
member2 = {input() for _ in range(g2)}

same = [*(member1 & member2)]

if len(same) > 0:
    print(*sorted(same, reverse=True), sep="\n")
else:
    print("Nope")
