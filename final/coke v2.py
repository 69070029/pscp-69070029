"""Coke V2"""
per = int(input())
cap = int(input())
per_new = int(input())
want = int(input())

if not cap or not want:
    print(per * want)
else:
    exchange = (want - 1) // cap
    normal = want - exchange
    print(normal * per + exchange * per_new)
