"""bank"""
def main():
    """input"""
    amount = int(input())
    ten = amount % 10
    five = ten % 5
    two = five % 2
    print(f"10 = {amount // 10}")
    print(f"5 = {ten // 5}")
    print(f"2 = {five // 2}")
    print(f"1 = {two // 1}")

main()
