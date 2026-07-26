"""เหมือนกันหมด"""
def main():
    """input"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if num1 == num2 and num2 == num3 and num1 == num3:
        print("all the same")
    elif num1 != num2 and num2 != num3 and num1 != num3:
        print("all different")
    else:
        print("neither")

main()
