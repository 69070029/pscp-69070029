"""missing number"""
last = int(input())
num = []

while True:
    num.append(int(input()))

    if 0 in num:
        num.remove(0)
        break

num = sorted(num)

should = set()

should.update(x for x in range(1, last + 1))

ans = sorted(should - set(num))

print(*ans, sep="\n")
