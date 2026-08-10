"""[LEARNING LOGS] เกมสะสมแต้ม"""
def main():
    """input"""
    keerob = int(input())
    point = 0

    for _ in range(keerob):
        change = input()
        if change == "+":
            point += 10
        elif change == "-":
            point -= 5
    print(point)

main()
