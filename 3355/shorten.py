"""shorten"""
lek = []

while True:
    n = int(input())
    if n == -1:
        break

    lek.append(n)

if not lek:
    print("")
else:
    start = lek[0]
    end = lek[0]

    result = []

    for num in lek[1:]:
        if num == end + 1:
            end = num
            if num == lek[-1]:
                result.append(f"{start}-{end}")
        else:
            if start == end:
                result.append(start)
            else:
                result.append(f"{start}-{end}")
            if num == lek[-1]:
                result.append(num)

            start = end = num

    if lek[0] == lek[-1]:
        print(lek[0])
    else:
        print(*result, sep=", ")
