"""noodle"""
price = int(input())
pay = int(input())

if pay < price:
    print("Need more cash!")
elif pay == price:
    print("Good!")
else:
    print(pay - price)
