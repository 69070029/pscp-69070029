"""sairahut"""
num = input()

if num[:2] != "68" or num[2:4] != "07" or num[-4:] < "0001" or num[-4:] > "0328":
    print("No")
else:
    print("Yes")
