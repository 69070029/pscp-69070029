"""ผ่าน/ไม่ผ่าน"""
mid = int(input())
last = int(input())

total = mid + last

if total >= 50:
    print(total)
    print("pass")
else:
    print(total)
    print("fail")
