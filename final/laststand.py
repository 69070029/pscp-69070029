"""last stand"""
lek = list(input().split(","))

for i, num in enumerate(lek):
    if i == len(lek) - 1:
        print(num[-2])
    else:
        print(num[-1])
