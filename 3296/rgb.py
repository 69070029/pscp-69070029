"""RGB"""
import math

r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())

print(math.floor((r1 + r2) / 2), math.floor((g1 + g2) / 2), math.floor((b1 + b2) / 2))
