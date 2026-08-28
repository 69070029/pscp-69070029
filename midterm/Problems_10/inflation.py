"""inflation"""
import math

def main():
    """input"""
    price = float(input())
    year = int(input())

    for _ in range(year):
        price += price * 0.0381

    print(f"{price:.2f}")
main()
