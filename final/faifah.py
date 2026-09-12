"""faifa"""
unit = int(input())

if 1 <= unit <= 10:
    pay = 5 * unit
elif 11 <= unit <= 50:
    pay = 50 + (7 * unit)
elif 51 <= unit <= 100:
    pay = 330 + (10 * unit)
elif 101 <= unit <= 200:
    pay = 830 + (12 * unit)
else:
    pay = 2030 + (15 * unit)

pay += pay * 0.07
pay += unit / 2

print(f"{pay:.1f}")
