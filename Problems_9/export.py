"""สินค้าส่งออก"""
n = int(input())
total = 0
even = 0
odd = 0

for i in range(1, n + 1):
    i = int(input())
    total += i
    if i % 2:
        odd += 1
    else:
        even += 1
print(f"SUM {total}")
print(f"EVEN {even}")
print(f"ODD {odd}")
