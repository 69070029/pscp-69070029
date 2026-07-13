"""Heron's Formula"""
def main():
    """ใส่เลข"""
    a = float(input())
    b = float(input())
    c = float(input())

    s = (a + b + c)/2

    answer = (s * (s-a) * (s-b) * (s-c))**(1/2)

    print(f"{answer:.3f}")

main()
