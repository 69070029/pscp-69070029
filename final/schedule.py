"""teaching schedule"""
amount = int(input())
time = int(input())

total = amount * time
hr = total // 60
minute = total % 60

if total <= 0:
    print("No teaching")
elif not hr:
    print(f"{minute} minute")
elif not minute:
    print(f"{hr} hours")
else:
    print(f"{hr} hours {minute} minute")
