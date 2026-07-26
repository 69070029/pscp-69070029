"""เพิ่ม/ลด"""
def main():
    """input"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if num1 > num2 > num3:
        print("decreasing")
    elif num1 < num2 < num3:
        print("increasing")
    else:
        print("neither")

main()
