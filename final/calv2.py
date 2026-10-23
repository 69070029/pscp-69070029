"""calculator v2"""
lek = int(input())

digit = 0
start = 1
length = 1

while start <= lek:
    end = min(lek, start * 10 - 1)
    digit += (end-start+1) * length
    start *= 10
    length += 1

if lek == 1:
    print(1)
else:
    print(lek + digit)
