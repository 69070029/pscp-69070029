"""picknum"""
lek = list(map(int, input().split()))

po = 0
ne = 0
ze = 0

for num in lek:
    if not num:
        ze += 1
    elif num > 0:
        po += 1
    else:
        ne += 1

print(f"Positive: {po}")
print(f"Negative: {ne}")
print(f"Zero: {ze}")
