"""Longer"""
import math

r = float(input())
a = float(input())
b = float(input())

circle = 2 * math.pi * r
rectangle = (2 * a) + (2 * b)

if circle > rectangle:
    print("Circle is longer")
    print(f"{circle - rectangle:.5f}")
elif rectangle > circle:
    print("Rectangle is longer")
    print(f"{rectangle - circle:.5f}")
else:
    print("Equal")
    print("0.00000")
