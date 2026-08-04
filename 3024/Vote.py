"""Surprising Vote"""
def main():
    """input"""
    total = float(input())
    high = float(input())
    remain = total - high
    least = remain - high

    if least < 0:
        least = 0

    if high - least > 2:
        ans = "Surprising"
    else:
        ans = "Not surprising"

    print(ans)

main()
