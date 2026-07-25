"""input"""
a = int(input())
b = int(input())
goal = int(input())

how_much_b = goal // 5 #ใช้กี่ก้อน

remain = goal - (how_much_b * 5) #เหลือความยาวอีกเท่าไหร่

how_much_a = remain // 1 #ใช้ a กี่ก้อน

if how_much_b > b:
    ANS = -1
elif how_much_a > a:
    ANS = -1
else:
    ANS = how_much_a

print(ANS)
