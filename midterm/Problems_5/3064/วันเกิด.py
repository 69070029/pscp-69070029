"""วันเกิด"""
from datetime import date

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

date_1 = date(y1, m1, d1)
date_2 = date(y2, m2, d2)

if abs(date_1 - date_2).days <= 7:
    print("0")
else:
    if date_1 > date_2:
        print("2")
    else:
        print("1")
