"""GCD N"""
import math

taorai = int(input())

num = []

for _ in range(taorai):
    num.append(int(input()))

print(math.gcd(*num))
