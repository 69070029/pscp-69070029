"""resistor"""
num1 = input()
num2 = input()
koon = input()
per = input()

rahus = {
    "Black": "0", "Brown": "1", "Red": "2",
    "Orange": "3", "Yellow": "4", "Green": "5",
    "Blue": "6", "Purple": "7", "Grey": "8", "White": "9"}

multi = {
    "Black": 1, "Brown": 10, "Red": 100,
    "Orange": 1000, "Yellow": 10000, "Green": 100000,
    "Blue": 10**6, "Purple": 10**7, "Gold": 0.1, "Silver": 0.01}

tolerance = {
    "Brown": 1, "Red": 2, "Green": 0.5, 
    "Blue": 0.25, "Purple": 0.1, "Grey": 0.05, 
    "Gold": 5, "Silver": 10}

if num1 not in rahus or num2 not in rahus or koon not in multi or per not in tolerance:
    print("Error")
else:
    print(f"{((int(rahus[num1] + rahus[num2]) * multi[koon]) * (100 - tolerance[per])) / 100:.4f}")
    print(f"{((int(rahus[num1] + rahus[num2]) * multi[koon]) * (100 + tolerance[per])) / 100:.4f}")
