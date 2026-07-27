"""Surprising Vote"""
def main():
    """input"""
    sum = int(input())
    high = int(input())
    remain = sum - high

    x = max(remain)
    y = min(remain)

    print(x)

main()

