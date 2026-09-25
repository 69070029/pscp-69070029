"""faifa"""
unit = int(input())
pay = 0

for i in range(1, unit + 1):
    if 1 <= i <= 10:
        pay += 5
    elif 11 <= i <= 50:
        pay += 7
    elif 51 <= i <= 100:
        pay += 10
    elif 101 <= i <= 200:
        pay += 12
    else:
        pay += 15
ft = unit * 0.5
VAT = pay * 0.07
total = (pay + VAT + ft) + 0.001

print(f"{total:.1f}")
