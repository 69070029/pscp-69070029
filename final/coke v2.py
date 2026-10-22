"""Coke V2"""
per = int(input())
cap = int(input())
per_new = int(input())
want = int(input())

exchange = 0
taorai = 0
pay = 0

while taorai < want:
    if exchange >= cap:
        pay += per_new
        exchange -= cap
    else:
        pay += per

    exchange += 1
    taorai += 1

print(pay)
