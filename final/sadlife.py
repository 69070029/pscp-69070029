"""tuple's sad life"""
rubna = tuple(input().split())
want = input()

taorai = rubna.count(want)
pos = rubna.index(want)

oneline = [pos] * taorai
for _ in range(taorai):
    print(*oneline)
