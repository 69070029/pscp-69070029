"""teaching schedule"""
amount = int(input())
time = int(input())

total = amount * time
hr = total // 60
min = total % 60

if not hr:
    print(f"{min} minute")
elif not min:
    print(f"{hr} hours")
elif total <= 0:
    print("No teaching")
else:
    print(f"{hr} hours {min} minute")
