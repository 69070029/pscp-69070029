"""minimum (4)"""
def main():
    """input"""
    taorai = int(input())
    keetua = []

    for i in range(taorai):
        number = int(input())
        keetua.append(number)

    if len(keetua) == 1:
        print(keetua[0])
    elif len(keetua) == 2:
        if keetua[0] < keetua[1]:
            print(keetua[0])
        else:
            print(keetua[1])
    elif len(keetua) == 3:
        if keetua[0] < keetua[1] and keetua[0] < keetua[2]:
            print(keetua[0])
        elif keetua[1] < keetua[2]:
            print(keetua[1])
        else:
            print(keetua[2])        
    elif len(keetua) == 4:
        if keetua[0] < keetua[1] and keetua[0] < keetua[2] and keetua[0] < keetua[3]:
            print(keetua[0])
        elif keetua[1] < keetua[2] and keetua[1] < keetua[3]:
            print(keetua[1])
        elif keetua[2] < keetua[3]:
            print(keetua[2])
        else:
            print(keetua[3])

main()
