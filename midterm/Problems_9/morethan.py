"""ผลรวมของค่าที่มากกว่า"""
def main():
    """input"""
    koo = int(input())

    more = []

    for _ in range(koo):
        num1 = int(input())
        num2 = int(input())

        if (num1 > num2) or (num1 == num2):
            more.append(num1)
        else:
            more.append(num2)

    if len(more) == 1:
        print(more[0])
    else:
        print(*more, sep=" + ", end=" = ")
        print(sum(more))
main()
