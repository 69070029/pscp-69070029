"""* X"""
number = int(input())
text = []
for i in range(1, number + 1):
    if i % 5:
        ANS = "*"
        text.append(ANS)
    else:
        ANS = "X"
        text.append(ANS)
print(*text, sep="")
