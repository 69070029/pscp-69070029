"""hint"""
def check(num, op, target):
    """operator"""
    if op == "==":
        return num == target
    if op == "!=":
        return num != target
    if op == ">":
        return num > target
    if op == ">=":
        return num >= target
    if op == "<":
        return num < target
    if op == "<=":
        return num <= target

    return False

i1, nuay = input().split()
i2, sib = input().split()
i3, roi = input().split()

nuay = int(nuay)
sib = int(sib)
roi = int(roi)

for i in range(1000):
    ans = f"{i:03d}"

    if check(int(ans[2]), i1, nuay) \
    and check(int(ans[1]), i2, sib) \
    and check(int(ans[0]), i3, roi):
        print(ans)
