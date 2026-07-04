#ระบุตัวเลข
RA = int(input('ระบุ RA: '))
RB = int(input('ระบุ RB: '))
AB = input('เป็น A หรือ B: ')

#ให้คำตอบ
if AB == 'A':
    ans = 1/(1+10**((RB-RA)/400))
elif AB == 'B':
    ans = 1/(1+10**((RA-RB)/400))

print(round(ans, 2))