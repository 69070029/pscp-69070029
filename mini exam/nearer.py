"""itim"""
alice = int(input())
bob = int(input())
car = int(input())

diff_a = abs(car - alice)
diff_b = abs(car - bob)

if diff_a < diff_b:
    print(f"Alice {diff_a}")
elif diff_a > diff_b:
    print(f"Bob {diff_b}")
else:
    print(f"Sundaes {diff_a}")
